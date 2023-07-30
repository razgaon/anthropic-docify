import logging
import pandas as pd
from agent import get_improved_page
from utils import LANGCHAIN_BASE, save_output, get_langchain_docs_url
from tqdm import tqdm
from vector_store import pinecone_vector_stores, get_index
from llama_index.retrievers import VectorIndexRetriever
import xml.etree.ElementTree as ET

logging.basicConfig(
    format="%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)

def get_args(reference_df):
    reference_doc = reference_df["content"].iloc[0]

    reference_page_name = (
        reference_df["url"].iloc[0].split(LANGCHAIN_BASE + "/")[1]
    )  # will return something like /modules/chains/how_to/memory.md'
    reference_page_name = reference_page_name.replace(
        "/", "-"
    )  # Prevents issue with writing the file
    # If the reference page name is empty, it will default to the index page
    if reference_page_name == "":
        reference_page_name = "index"

    index = get_index(pinecone_vector_stores["official"])
    retriever = VectorIndexRetriever(index=index, similarity_top_k=5)
    similar_nodes_with_scores = retriever.retrieve(reference_doc)
    similar_nodes = [n.node for n in similar_nodes_with_scores]
    text_from_nodes = [node.text for node in similar_nodes]
    context = "\n\n".join(text_from_nodes)
    return reference_doc, context, reference_page_name


def main():
    df = pd.read_csv("./data/data.csv")
    urls = get_langchain_docs_url()

    for url in tqdm(urls):
        # Trigger deployment
        try:
            reference_df = df[df["url"] == url]
            reference_doc, context, reference_page_name = get_args(reference_df)

            output = get_improved_page(reference_doc, context, reference_page_name)

            name_to_save = reference_page_name.replace("-", "/").replace('_', ' ')
            
            if name_to_save.endswith("/"):
                name_to_save += "index"

            save_output(f"./output/v0/{reference_page_name}.md", reference_doc)
            save_output(f'../docs_pages/pages/{name_to_save}.md', output)
            
        except Exception as e:
            print(f'Encountered an error improving page {url=}: {e}')


if __name__ == "__main__":
    main()

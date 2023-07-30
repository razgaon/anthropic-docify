import os
import logging
import pandas as pd
from agent import get_improved_page
from utils import LANGCHAIN_BASE, save_output, get_langchain_docs_url, get_all_paths
from tqdm import tqdm
from vector_store import pinecone_vector_stores, get_index
from llama_index.retrievers import VectorIndexRetriever
import tiktoken

logging.basicConfig(
    format="%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)

SAVE_DIR = "langdocs/docs/"

def get_args(reference_df):
    reference_doc = reference_df["content"].iloc[0]
    
    encoding = tiktoken.get_encoding('cl100k_base')
    num_tokens = len(encoding.encode(reference_doc))
    retrievel_ref_doc = reference_doc
    
    if num_tokens > 8000:
        print("Split large reference doc")
        retrievel_ref_doc = reference_doc[:len(reference_doc)//2]
    
    reference_page_name = (
        reference_df["url"].iloc[0].split(LANGCHAIN_BASE + "/")[1]
    )  # will return something like /modules/chains/how_to/memory.md'
    
    # If the reference page name is empty, it will default to the index page
    if reference_page_name[-1] == "/":
        reference_page_name += "index"

    index = get_index(pinecone_vector_stores["official"])
    retriever = VectorIndexRetriever(index=index, similarity_top_k=5)
    
    similar_nodes_with_scores = retriever.retrieve(retrievel_ref_doc)
    similar_nodes = [n.node for n in similar_nodes_with_scores]
    text_from_nodes = [node.text for node in similar_nodes]
    
    context = "\n\n".join(text_from_nodes)
    return reference_doc, context, reference_page_name


def main():
    skip_existing = True

    df = pd.read_csv("src/data/data.csv")
    urls = get_langchain_docs_url()

    errors = []
    for url in tqdm(urls):
        # Trigger deployment
        try:
            reference_df = df[df["url"] == url]
            reference_doc, context, reference_page_name = get_args(reference_df)
            
            output_path = f"{SAVE_DIR}/{reference_page_name}.md"
            if skip_existing and os.path.isfile(output_path):
                print(f"File {reference_page_name} already exists")
                continue

            output = get_improved_page(reference_doc, context, reference_page_name)

            save_output(f"src/output/v0/{reference_page_name}.md", reference_doc)
            save_output(output_path, output)
            
        except Exception as e:
            errors.append(url)
            print(f"Encountered an error for url {url} improving page: {e}")


if __name__ == "__main__":
    main()

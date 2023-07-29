import logging
import chromadb
import pandas as pd
from agent import get_improved_page
from utils import LANGCHAIN_BASE
chroma_client = chromadb.PersistentClient()


logging.basicConfig(
    format="%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)



def main():
    df = pd.read_csv('./data/data.csv')
    
    chroma_collection = chroma_client.get_collection(name="official")
    
    x = chroma_collection.query(query_texts=["What is a langchain retriever?"], n_results=8)
    url = 'https://python.langchain.com/docs/modules/chains/how_to/memory'
    
    context_list = x.get("documents")[0]
    context = '\n\n'.join(context_list)
    
    reference_df = df[df['url'] == url]
    
    reference_doc = reference_df['content']
    reference_page_name = reference_df['url'].split(LANGCHAIN_BASE)[1]
    
    
    
    improved = get_improved_page(reference_doc, context, reference_page_name)
    
    with(open(f'./output/final/{reference_page_name}.md', 'w')) as f:
        f.write(improved)


if __name__ == "__main__":
    main()

import logging
import chromadb
import pandas as pd
from agent import get_improved_page
from utils import LANGCHAIN_BASE, save_output, get_all_paths

chroma_client = chromadb.PersistentClient()


logging.basicConfig(
    format="%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)

def get_args(chroma_collection, reference_df):
    reference_doc = reference_df['content'].iloc[0] 
    reference_page_name = reference_df['url'].iloc[0].split(LANGCHAIN_BASE + "/")[1] # will return something like /modules/chains/how_to/memory.md'
    reference_page_name = reference_page_name.replace("/", '-') # Prevents issue with writing the file
    similar = chroma_collection.query(query_texts=[reference_doc], n_results=5)
    context_list = similar.get("documents")[0]
    context = '\n\n'.join(context_list)
    
    return reference_doc, context, reference_page_name

def main():
    df = pd.read_csv('./data/data.csv')
    urls = get_all_paths()    
    chroma_collection = chroma_client.get_collection(name="official")
    
    for url in urls:
        
        reference_df = df[df['url'] == url]
        reference_doc, context, reference_page_name = get_args(reference_df)
        
        get_improved_page(reference_doc, context, reference_page_name)
        
        save_output(f'./output/v0/{reference_page_name}.md', reference_doc)

if __name__ == "__main__":
    main()

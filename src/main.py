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
    url = 'https://python.langchain.com/docs/modules/chains/how_to/memory'
    
    reference_df = df[df['url'] == url]
    
    # x = chroma_collection.get(where={"url": url})
    
    reference_doc = reference_df['content'].iloc[0] 
    reference_page_name = reference_df['url'].iloc[0].split(LANGCHAIN_BASE + "/")[1] # will return something like /modules/chains/how_to/memory.md'
    reference_page_name = reference_page_name.replace("/", '-') # Prevents issue with writing the file
    
    x = chroma_collection.query(query_texts=[reference_doc], n_results=8)
    
    context_list = x.get("documents")[0]
    context = '\n\n'.join(context_list)
    
    improved = get_improved_page(reference_doc, context, reference_page_name)
    
    with(open(f'./output/v0/{reference_page_name}.md', 'w')) as f:
        f.write(reference_doc)
        
    with(open(f'./output/final/{reference_page_name}.md', 'w')) as f:
        f.write(improved)


if __name__ == "__main__":
    main()

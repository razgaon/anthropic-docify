import pickle
import pandas as pd
from utils import get_all_paths
from tqdm import tqdm
from crawler import WebpageCrawler, SourceType
from chroma import add_collection
    
    


def crawl():
    directory = "/Users/razgaon/Desktop/langchain/docs/docs_skeleton/docs"  # replace with your directory path
    langchain_paths = get_all_paths(directory)
    errored = []
    urls = [*langchain_paths]

    sources = []
    for url in tqdm(urls):
        print(f"Scraping {url}...")
        crawler = WebpageCrawler(
            source_type=SourceType.Official, use_unstructured=False
        )
        try:
            sources.append(crawler.generate_row(url))
        except:
            errored.append(url)
            print(f"Error on {url}")
            
    add_collection("official", sources)
    # TO CSV
    # df = pd.DataFrame(sources)
    # df.to_csv("./data/data.csv", index=False)

    # Keep track of urls that errored
    with open("./data/errored.pickle", "wb") as file:
        pickle.dump(errored, file)
    
if __name__ == "__main__":
    crawl()
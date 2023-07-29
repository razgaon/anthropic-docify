from crawler import WebpageCrawler, SourceType
import logging
import pandas as pd
import os
import pickle
from tqdm import tqdm
from chroma import create_chroma_client, add_collection


def get_all_paths(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mdx"):
                paths.append(
                    "https://python.langchain.com/docs"
                    + (
                        os.path.join(root, file)
                        .replace(directory, "")
                        .replace(".mdx", "")
                        .replace("index", "")
                    )
                )

    return paths


logging.basicConfig(
    format="%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)


def main():
    directory = "/Users/razgaon/Desktop/langchain/docs/docs_skeleton/docs"  # replace with your directory path
    langchain_paths = get_all_paths(directory)
    count = len(langchain_paths)
    errored = []
    urls = [*langchain_paths]
    rows = []

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

    # TO CSV HERE
    # df = pd.DataFrame(rows)
    # df.to_csv("./data/data.csv", index=False)

    # # Keep track of urls that errored
    # with open("./data/errored.pickle", "wb") as file:
    #     pickle.dump(errored, file)

    chroma = create_chroma_client()
    collection = add_collection("official", sources)
    results = collection.query(query_texts=["This is a query document"], n_results=2)


if __name__ == "__main__":
    main()

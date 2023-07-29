import logging
import os, sys
from typing import List
import chromadb
import dataclasses
from llama_index import Document, VectorStoreIndex, StorageContext
from llama_index.vector_stores import ChromaVectorStore
from custom_types import Source, SourceType
from crawler import WebpageCrawler, SourceType
from tqdm import tqdm


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

chroma_client = chromadb.PersistentClient()


def get_urls(sources: List[Source]):
    return [s.url for s in sources]


def get_contents(sources: List[Source]):
    return [s.content for s in sources]


def get_documents(sources: List[Source]):
    return [Document(text=s.content) for s in sources]


def get_metadatas(sources: List[Source]):
    return [s.metadata for s in sources]


def add_collection(name: str, sources: List[Source]):
    chroma_collection = chroma_client.get_or_create_collection(name)
    urls = get_urls(sources)
    documents = get_documents(sources)
    metadatas = [dataclasses.asdict(s.metadata) for s in sources]
    chroma_collection.add(
        ids=urls,
        documents=documents,
        metadatas=metadatas,
    )
    return chroma_collection


def create_langchain_collection():
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

    directory = "/Users/allengu/langchain/docs/docs_skeleton/docs"  # replace with your directory path
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
        except Exception as e:
            errored.append(url)
            print(f"Error on {url}, {e}")

    # TO CSV HERE
    # df = pd.DataFrame(rows)
    # df.to_csv("./data/data.csv", index=False)

    # # Keep track of urls that errored
    # with open("./data/errored.pickle", "wb") as file:
    #     pickle.dump(errored, file)

    collection = add_collection("official", sources)
    return collection


if __name__ == "__main__":
    collection = chroma_client.get_collection(name="official")
    print(collection.peek())
    # results = collection.query(query_texts=["How do I use vector stores?"], n_results=1)
    # print(results)

import logging
import sys
from typing import Any, List
import chromadb
import dataclasses
from utils import get_all_paths
from llama_index import (
    Document,
    StorageContext,
    ServiceContext,
    VectorStoreIndex,
    LangchainEmbedding,
)
from llama_index.embeddings import OpenAIEmbedding
from llama_index.vector_stores import ChromaVectorStore
from llama_index.node_parser import SimpleNodeParser
from langchain.embeddings import OpenAIEmbeddings
from custom_types import Source, SourceType
from crawler import WebpageCrawler, SourceType
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

chroma_client = chromadb.PersistentClient()
embed_model = LangchainEmbedding(OpenAIEmbeddings())


def get_urls(sources: List[Source]):
    return [s.url for s in sources]


def get_contents(sources: List[Source]):
    return [s.content for s in sources]


def get_documents(sources: List[Source]):
    return [
        Document(text=s.content, embedding=embed_model.get_text_embedding(s.content))
        for s in sources
    ]


def get_nodes(documents: List[Document]):
    parser = SimpleNodeParser()
    nodes = parser.get_nodes_from_documents(documents)


def get_metadatas(sources: List[Source]):
    return [s.metadata for s in sources]


def create_index(name: str, sources: List[Source] = []):
    chroma_collection = chroma_client.get_or_create_collection(name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    service_context = ServiceContext.from_defaults(
        embed_model=embed_model, chunk_size=8191
    )
    documents = get_documents(sources)
    index = VectorStoreIndex.from_documents(
        documents=documents,
        storage_context=storage_context,
        service_context=service_context,
    )
    return index


def get_index(name: str):
    chroma_collection = chroma_client.get_collection(name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    return VectorStoreIndex.from_vector_store(vector_store=vector_store)


def create_official_langchain_index():
    directory = "/Users/allengu/langchain/docs/docs_skeleton/docs"  # replace with your directory path
    langchain_paths = get_all_paths(directory)[:]
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

    index = create_index("official", sources)
    return index


if __name__ == "__main__":
    # chroma_client.delete_collection("official")
    create_official_langchain_index()

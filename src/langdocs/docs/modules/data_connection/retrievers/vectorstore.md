

# Vector Store-Backed Retriever

A vector store retriever allows retrieving documents from a vector store index using semantic similarity search. It wraps a VectorStore to conform to the Retriever interface in Langchain. Vector store retrievers enable efficient semantic search on large datasets.

## Introduction

Vector store retrievers provide a balance between scalability, speed, and accuracy compared to other retriever types like sparse retrievers (TF-IDF) and dense retrievers (DPR). They are a good choice when working with large, dynamic datasets that require fast indexing and efficient document updates.

## Usage

To use a vector store retriever, first instantiate a VectorStore. For example, with FAISS:

```python
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

embedding_fn = OpenAIEmbeddings() 
index = faiss.IndexFlatL2(embedding_fn.get_embedding_size())
vectorstore = FAISS(embedding_fn, index)
```

Then convert the VectorStore to a Retriever:

```python
retriever = vectorstore.as_retriever()
```

Now `retriever` can be used to find relevant documents:

```python
docs = retriever.get_relevant_documents("What did the president say about Ketanji Brown Jackson?")
```

## Tuning Retrieval

When creating the retriever, you can specify arguments like `k` and `score_threshold` to control retrieval:

```python
retriever = vectorstore.as_retriever(k=5, score_threshold=0.8)  
```

- Higher `k` increases recall at the cost of less relevant results.
- Higher `score_threshold` improves precision but lowers recall.

Good starting values are `k=10` and `score_threshold=0.5`. Tune as needed for your use case.

## Comparison to Other Retrievers

Compared to sparse retrievers like TF-IDF, vector store retrievers enable semantic search using dense embeddings. They scale better to large datasets but have higher latency per query.

Compared to dense retrievers like DPR, vector stores offer faster indexing and efficient document updates. But they may be less accurate than end-to-end trained dense retrievers.

Overall, vector store retrievers strike a balance between scalability, speed, and accuracy. They are a good choice when working with large, dynamic datasets that require efficient indexing and updates.


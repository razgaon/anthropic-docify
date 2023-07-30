
# Vector Stores

## Introduction

Vector stores are databases optimized for storing and querying vector embeddings of text. They allow storing embedding vectors of documents and then quickly finding similar vectors for a query. 

Vector stores are often run as separate services that require IO operations to connect to. Therefore, they can benefit from asynchronous calls to avoid blocking while waiting for responses. Using async operations also enables easy integration with asynchronous Python frameworks like FastAPI.

## Asynchronous Operations

Langchain supports calling vector stores asynchronously using async methods prefixed with `a`. 

For example, to asynchronously create a Qdrant vector store:

```python
db = await Qdrant.afrom_documents(documents, embeddings, "http://localhost:6333")
```

To do an asynchronous similarity search:

```python
query = "What did the president say about Ketanji Brown Jackson"
docs = await db.asimilarity_search(query)
```

We can also asynchronously search by vector:

```python  
embedding_vector = embeddings.embed_query(query)
docs = await db.asimilarity_search_by_vector(embedding_vector)
```

For asynchronous maximum marginal relevance search:

```python
found_docs = await qdrant.amax_marginal_relevance_search(query, k=2, fetch_k=10) 
```

## Benefits

Calling vector stores asynchronously provides two key benefits:

1. Improved performance by not blocking - async calls allow other code to execute while waiting for IO operations to complete rather than blocking.

2. Easy integration with async frameworks like FastAPI - async vector store calls fit cleanly into async codebases.

Using asynchronous operations allows vector stores to provide fast, non-blocking search while integrating smoothly into modern async Python applications.


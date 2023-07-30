

# Asynchronous Operations

Vector stores are usually run as a separate service that requires some IO operations, and therefore they might be called asynchronously. That gives performance benefits as you don't waste time waiting for responses from external services. That might also be important if you work with an asynchronous framework, such as FastAPI.

Langchain supports async operation on vector stores. All the methods might be called using their async counterparts, with the prefix `a`, meaning `async`.

For example, to asynchronously create a Qdrant vector store from documents:

```python
db = await Qdrant.afrom_documents(documents, embeddings, "http://localhost:6333")
```

To do an asynchronous similarity search:

```python  
query = "What did the president say about Ketanji Brown Jackson"
docs = await db.asimilarity_search(query)
```

We can also do an asynchronous search by vector:

```python
embedding_vector = embeddings.embed_query(query)  
docs = await db.asimilarity_search_by_vector(embedding_vector)
```

Asynchronous maximum marginal relevance search is also supported:

```python
found_docs = await qdrant.amax_marginal_relevance_search(query, k=2, fetch_k=10)
```

Calling vector stores asynchronously improves performance by not blocking, and enables integration with asynchronous frameworks like FastAPI.


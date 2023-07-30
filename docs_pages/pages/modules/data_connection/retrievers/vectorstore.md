

# Vector Store-Backed Retriever

A vector store retriever uses a vector store to quickly retrieve semantically similar documents for a query. It wraps a vector store to conform to the Retriever interface in LangChain.

Vector store retrievers are useful when you have a large corpus of texts, and need to efficiently find relevant information. They provide much faster retrieval than dense retrievers at scale, while maintaining high accuracy.

## Comparison to Other Retrievers

Compared to dense retrievers like the DensePassageRetriever, vector stores have the advantage of reduced latency and the ability to scale to massive document collections. They can retrieve results in milliseconds versus seconds.

The tradeoff is that they have slightly lower precision/recall than dense retrievers in some cases. However, for most use cases, their accuracy is still very high while providing faster performance.

In general, vector stores are a better choice when:

- You need low latency retrieval for large document collections
- Your documents have semantic similarity that can be captured with embeddings
- You care more about speed and scalability than perfect precision/recall

Dense retrievers are better when you need maximum precision/recall and have a smaller corpus.

## Basic Usage

Using a vector store retriever follows a simple workflow:

1. Load documents
2. Generate embeddings 
3. Index into vector store 
4. Wrap as a retriever

Let's walk through an example loading some sample documents from a text file:

```python
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings  
from langchain.vectorstores import FAISS

docs = TextLoader("./documents.txt").load() 

embeddings = OpenAIEmbeddings()
indexed_docs = FAISS.from_documents(docs, embeddings)

retriever = indexed_docs.as_retriever()
```

We can now use this retriever to find relevant documents:

```python
results = retriever.get_relevant_documents("Who is the president of the United States?")
```

## Configuration and Parameter Tuning

There are several parameters that can be tuned when creating the vector store retriever:

**k** - The number of documents to retrieve per query. Higher k values give higher recall but slower performance. For example, setting k=10 might give 90% recall but take 500ms per query. k=5 might take 100ms but only give 50% recall.

**score_threshold** - Only return documents with a score above this threshold. Useful for precision but lowers recall. Setting this to 0.5 might increase precision to 95% but lower recall to 10%.

**search_type** - Specify alternative search algorithms like MMR.

Tuning these parameters allows trading off between precision, recall and latency. Some example configurations:

```python
# High precision configuration 
retriever = indexed_docs.as_retriever(k=5, score_threshold=0.8)  

# High recall configuration
retriever = indexed_docs.as_retriever(k=20, score_threshold=0.2)
```

## Best Practices

Here are some tips for optimizing vector store retriever performance:

- Use smaller embedding sizes (e.g. 256 vs 1024) to improve indexing and search speed
- Preprocess documents to remove stopwords, shorten length, etc. This improves embedding quality.
- Experiment with different vector stores like FAISS, Pinecone, etc. Performance varies.
- Try approximate nearest neighbor algorithms like HNSW for faster search.
- Combine with a dense retriever for improved precision/recall.

Overall, vector store retrievers provide a scalable, low-latency solution for document retrieval when you need speed and accuracy. With some tuning and combining with other retrievers, they can reach very high levels of performance.


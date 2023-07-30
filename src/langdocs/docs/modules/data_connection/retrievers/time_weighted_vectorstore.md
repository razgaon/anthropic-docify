

# Time-weighted vector store retriever

## Introduction

The time-weighted vector store retriever is a retriever that combines semantic similarity search with time decay. Documents are scored based on:

```
semantic_similarity + (1.0 - decay_rate) ^ hours_passed
```

The `hours_passed` refers to the number of hours since the document was **last accessed**, not when it was first added. This means frequently accessed documents stay relevant for longer. 

The decay rate controls how quickly document relevance decays over time. Lower decay rates mean documents stay relevant for longer. Higher decay rates mean document relevance decays faster.

Below we walk through examples of using the time-weighted vector store retriever with different vector stores and decay rate values.

## Usage

First we need to initialize a vector store and retriever. This example shows FAISS, but other stores like Pinecone and Weaviate could also be used:

```python
import faiss  

from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings  
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain.vectorstores import FAISS

embeddings_model = OpenAIEmbeddings()

# Initialize FAISS vector store
embedding_size = 1536  
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(
    embeddings_model.embed_query, 
    index, 
    InMemoryDocstore({}), 
    {}
)

# Initialize retriever
retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectorstore, 
    decay_rate=0.5, 
    k=1
)
```

### Low Decay Rate

A low decay rate like 0.01 means documents stay relevant for a long time. This makes the retriever behave almost like a standard vector lookup.

```python
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)

retriever.add_documents([
    Document(page_content="hello world", metadata={"last_accessed_at": yesterday}) 
])

retriever.add_documents([
    Document(page_content="hello foo")
])

# "Hello world" is returned first even though it's older, because the decay rate is so low
retriever.get_relevant_documents("hello world") 
```

### High Decay Rate

A high decay rate like 0.99 means document relevance decays very quickly over time. This weights recency much more strongly.

```python
retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectorstore, 
    decay_rate=0.99, 
    k=1
)

yesterday = datetime.now() - timedelta(days=1)  

retriever.add_documents([
    Document(page_content="hello world", metadata={"last_accessed_at": yesterday})
])

retriever.add_documents([
    Document(page_content="hello foo") 
])

# "Hello foo" is returned first because "hello world" has decayed more due to time  
retriever.get_relevant_documents("hello world")
```

### Tuning the Decay Rate

The optimal decay rate depends on your use case. For frequently changing collections, a higher decay rate around 0.8-0.9 weights recent documents more. For static collections, a lower decay rate of 0.1-0.3 is likely better.

To tune the decay rate parameter:

- Start with a moderate value like 0.5
- Evaluate relevance over a sample set of queries 
- Adjust decay rate up or down and re-evaluate
- Repeat until you find the best balance for your needs

Monitor relevance over time and continue to tune as needed.

## Conclusion

The time-weighted vector store retriever provides a way to combine semantic similarity with recency. Tuning the decay rate allows customizing how document relevance decays over time.




# Time-weighted vector store retriever 

## Introduction

The time-weighted vector store retriever combines semantic similarity search with time decay to prioritize recent and frequently accessed documents. Documents are scored based on:

```
semantic_similarity + (1.0 - decay_rate)^hours_passed 
```

The `hours_passed` refers to the number of hours since the document was last accessed, not when it was first added. This gives frequently accessed documents higher scores.

This retriever can be useful compared to standard vector store retrievers when very recent and frequently accessed documents should be prioritized in results. The decay rate parameter provides flexibility to tune recency vs. semantic relevance.

Below we show examples of using the retriever with different decay rates and mocking time for testing.

## Usage 

First we need to initialize a vector store and define our retriever:

```python
# Code to initialize vector store 

# Define retriever
retriever = TimeWeightedVectorStoreRetriever(
    vectorstore=vectorstore, 
    decay_rate=0.5,
    k=1  
)
```

### Low decay rate

A low `decay_rate` like 0.1 means documents will persist in memory longer. A rate of 0 means documents will never be forgotten.

```python
# Example with low decay rate
```

This is useful when semantic relevance is more important than recency. The retriever will behave similar to a standard vector retriever.

### High decay rate

A high `decay_rate` like 0.9 means documents will be forgotten quickly. A rate of 1 means all documents have a recency score of 0.

```python
# Example with high decay rate 
```

This is useful when very recent documents are critical. The retriever will heavily prioritize recent documents.

### Mocking time

For testing, you can mock the time component:

```python 
# Example mocking time
```

## Tuning decay rate

The decay rate parameter controls the balance between semantic relevance and recency. Some guidelines for tuning:

- **Chatbots**: Lower decay rate around 0.5 to keep conversations coherent over time
- **Search**: Higher decay rate around 0.9 to surface breaking news
- **Slowly changing corpus**: Lower decay rate around 0.1 to keep docs relevant 
- **Frequently updated corpus**: Higher decay rate around 0.9 to surface new docs
- **Typical values** between 0.5 and 0.99

Experiment with different values based on your use case and frequency of new documents. 

## Conclusion

The time-weighted vector store retriever provides a way to combine semantic similarity with recency. It can be useful when very recent and frequently accessed documents should be prioritized in results. The decay rate parameter provides flexibility based on use cases.


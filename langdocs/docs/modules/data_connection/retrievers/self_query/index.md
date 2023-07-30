

# Self-Querying Retriever

## Overview

A self-querying retriever allows querying data through natural language. It uses a query-constructing language model to convert natural language queries into structured queries that can be executed against a vector index. This enables semantic search through natural language, as well as filtering on metadata.

## Getting Started

To use the self-query retriever, you need:

- `pinecone` and `lark` packages installed
- Pinecone API key and environment 

First, create a Pinecone vector index and populate it with document data:

```python
# Code to ingest documents into Pinecone index 
```

Then instantiate the retriever, providing metadata field descriptions and document content description:

```python
# Code to instantiate retriever
``` 

## Querying the Retriever

With the retriever instantiated, we can query it:

```python
# Query by relevance  
retriever.get_relevant_documents("What are some movies about dinosaurs?")

# Filter by metadata  
retriever.get_relevant_documents("Show me movies with rating over 8.5")

# Combination query and filter
retriever.get_relevant_documents("Did Greta Gerwig direct any movies about women?")
```

We can limit the number of results:

```python 
# Construct retriever with enable_limit=True 

retriever.get_relevant_documents("Give me two movies about dinosaurs")
```

The retriever handles complex boolean logic, filtering, and nested queries. See the [Advanced Queries](https://docs.langchain.dev/self_query#advanced-queries) section for examples. 

## Conclusion 

The self-query retriever enables natural language search over data by constructing structured queries from natural language. With the right setup, it's a powerful tool for semantic search and filtering. See the [full guide](https://docs.langchain.dev/self_query) for more details.


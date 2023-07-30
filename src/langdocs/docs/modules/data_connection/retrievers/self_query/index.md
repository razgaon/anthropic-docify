

# Self-Querying Retriever

## Overview

A self-querying retriever allows querying data stored in a vector index using natural language. It uses a query-constructing LLM to parse the natural language query into a structured query that can be executed against the vector index. This allows filtering and sorting results based on metadata fields as well as semantic similarity.

## Requirements

To use the self-query retriever, you need to have the following:

- `pinecone` Python package
- `lark` Python package for parsing
- Pinecone API key and Environment. See [Pinecone installation instructions](https://docs.pinecone.io/docs/quickstart) for details.

## Usage

First, create a Pinecone VectorStore and index your documents:

```python
import pinecone

# Create Pinecone index
index = pinecone.Index("my-index")

# Index documents
index.upsert(vectors=doc_vectors, ids=doc_ids) 
```

Then, instantiate the retriever by providing metadata field descriptions and document content description:

```python
from langchain.retrievers import SelfQueryRetriever

field_descriptions = [
    {"name": "genre", "type": "string"},
    {"name": "year", "type": "integer"} 
]
doc_description = "Brief movie summary"

retriever = SelfQueryRetriever(
    index, field_descriptions, doc_description
)
```

Now we can query the retriever:

```python 
retriever.get_relevant_documents(
    "What are some good sci-fi movies from the 80s?"
)
```

We can limit the number of results:

```python
retriever.get_relevant_documents(
    "What are two movies about dinosaurs?", k=2
)
```

The retriever handles complex queries with filters, comparisons, etc. See the API reference for more.

## Conclusion

The self-query retriever enables natural language search over vector indexes using metadata filters and text similarity. With the right setup, it can handle sophisticated queries. See the documentation for full usage details.


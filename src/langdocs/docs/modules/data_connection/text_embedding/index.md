

# Text Embedding Models

## Overview

The `Embeddings` class in LangChain provides a standard interface for working with different text embedding models like OpenAI Embeddings, HuggingFace Embeddings, Cohere Embeddings, etc.

Text embeddings convert text into vector representations. This enables semantic search by finding texts with similar vector representations in the vector space. For example, embedding a query and set of documents allows quickly finding the document closest to the query vector.

`Embeddings` exposes two main methods:

- `embed_documents` - Embed multiple texts
- `embed_query` - Embed a single text 

## Setup

To use the OpenAI Embeddings integration:

```python
pip install openai
```

Then set your API key:

```python
export OPENAI_API_KEY="..."
```

Or pass it directly:

```python
from langchain.embeddings import OpenAIEmbeddings

model = OpenAIEmbeddings(openai_api_key="...")
```

## Usage

### embed_documents

`embed_documents` embeds a list of texts.

```python
documents = ["Hello world", "How are you?", "What is the weather today?"]

embeddings = model.embed_documents(documents)
```

The output is a list of embedding vectors.

Use cases:

- Semantic search over a corpus of documents to find the most relevant result for a query
- Content recommendation based on vector similarity between documents

### embed_query

`embed_query` embeds a single text.

```python
query = "Where should I go on vacation?" 

embedding = model.embed_query(query)
```

The output is a single embedding vector.

Use cases:

- Semantic search - embed query then find closest document vectors
- Query understanding - analyze the embedding to determine user intent

You can customize the embedding size as needed:

```python
embedding = model.embed_query(query, embedding_size=1024)
```

## Available Classes

The following embedding integrations are available:

- [OpenAIEmbeddings](https://langchain.readthedocs.io/en/latest/llms.html#openai) - Uses OpenAI's text embedding API
- [HuggingFaceEmbeddings](https://langchain.readthedocs.io/en/latest/llms.html#huggingface) - Leverages HuggingFace's models and tokenizers 
- [CohereEmbeddings](https://langchain.readthedocs.io/en/latest/llms.html#cohere) - Uses Cohere's embedding API

See the documentation for each class for details on usage. Key differences include supported embedding models, token limits, and additional features.


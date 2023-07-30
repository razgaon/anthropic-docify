

# Text Embedding Models

## Introduction

Text embedding models are an essential component of natural language processing systems. They allow representing pieces of text as vectors in a continuous vector space. This enables semantic search, clustering, and other applications by comparing vector similarities rather than just lexical matches.

Popular embedding models include BERT, GPT-3, and word2vec. LangChain provides a standard interface to use these different embedding models through the `Embeddings` class.

## Getting Started

To start using text embeddings in LangChain, you will need to:

1. Install the OpenAI Python package:

```
pip install openai
```

2. Get an OpenAI API key from [here](https://platform.openai.com/account/api-keys) 

3. Set the API key as an environment variable:

```
export OPENAI_API_KEY="..."
```

Or pass the key directly when initializing the `OpenAIEmbeddings` class:

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(openai_api_key="...")
```

4. Import and initialize the `OpenAIEmbeddings` class:

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings()
```

## Key Methods

The `Embeddings` class exposes two key methods for generating embeddings:

### embed_documents

Converts a list of texts into vector representations:

```python
docs = ["Hello World!", "How are you?"]

embeddings = embeddings_model.embed_documents(docs)

print(len(embeddings)) # 2
print(len(embeddings[0])) # 1536
```

Documents are embedded together since some models use cross-document relationships.

### embed_query

Converts a single text into a vector representation:

```python  
query = "What was the greeting in the conversation?"

embedded_query = embeddings_model.embed_query(query)

print(len(embedded_query)) # 1536
```

The query is embedded individually so it can be compared against document vectors for semantic search.

Here is an example of using `embed_query` for semantic search:

```python
docs = ["Hello World!", "How are you?"]
doc_embeddings = embeddings_model.embed_documents(docs)

query = "What was the greeting in the conversation?"  
query_embedding = embeddings_model.embed_query(query)

# Compute cosine similarity
import scipy
most_similar_doc = scipy.spatial.distance.cdist([query_embedding], doc_embeddings).argmin()

print(docs[most_similar_doc]) # Hello World!
```

## Benefits

Some key benefits of using text embeddings include:

- Semantic search based on meaning rather than just keywords
- Ability to cluster documents and discover themes based on vector similarities
- Using pre-trained models like BERT rather than building from scratch
- Enables new applications like semantic code search, chatbots, recommender systems etc.

## Conclusion

The `Embeddings` class in LangChain provides a simple interface to generate vector representations of text using various embedding models. The key methods are `embed_documents` and `embed_query`. Text embeddings open up many possibilities for semantic applications and are a core building block of natural language systems.


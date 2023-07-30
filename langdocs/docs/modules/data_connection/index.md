

# Connecting External Data to Language Models

Many language model applications require connecting user-specific data that is not part of the model's training set. The data connection module in LangChain provides the building blocks to load, transform, store and query external data, enabling it to be used alongside language models.

## Overview

The main components of the data connection module are:

- **Document Loaders**: Load documents from diverse sources like local files, databases, APIs, etc.
- **Document Transformers**: Preprocess documents by splitting, converting to QA pairs, removing duplicates etc.
- **Text Embedding Models**: Convert text to vector representations capturing semantic meaning.
- **Vector Stores**: Index and store document vectors for efficient similarity search.  
- **Retrievers**: Query vector stores to find relevant documents.

![Data Connection Pipeline](data_connection.png)

These components allow building pipelines to bring in external data, process it, index it for fast retrieval, and query it from language models.

## Document Loaders

Document loaders allow loading data from various sources:

- Local files and folders
- Databases via SQLAlchemy 
- APIs via Requests
- Google Drive, S3 Buckets

Custom loaders can be written for other data sources.

**Examples:**

```python
# Load local text file
loader = DocumentLoader() 
docs = loader.load_from_path('data.txt')

# Load SQL database 
loader = PSQLDocumentLoader(table='documents', db_url='...')
docs = loader.load()
```

## Document Transformers

Transformers preprocess loaded documents before indexing. Useful transformations:

- Splitting documents into passages
- Converting documents to question-answer pairs
- Removing duplicate/irrelevant docs

Multiple transformers can be chained for complex pipelines.

**Examples:** 

```python
# Split documents
splitter = SplitDocuments(chunk_size=100)
docs = splitter.transform(docs)

# Convert to QA 
to_qa = Doc2QA()
docs = to_qa.transform(docs)
```

## Text Embedding Models

Embedders convert text to vector representations capturing semantic meaning, allowing vector similarity based retrieval.

LangChain supports models like SBERT, GPT-2 etc. Custom embeddings can also be provided. 

**Example:**

```python
embedder = SBERTEmbedding() 
embeddings = embedder.embed_documents(docs)
```

## Vector Stores

Vector stores like FAISS and Pinecone index embeddings for fast similarity search. Stores can persist data to disk.

**Example:** 

```python
store = FAISS()
store.add_documents(embeddings) 
```

## Retrievers 

Retrievers query vector stores to find relevant documents using text or embeddings. Different retrievers optimize for latency, accuracy etc.

**Example:**

```python
retriever = EmbeddingRetriever(vectorstore=store)
results = retriever.retrieve("What is LangChain?") 
```

The data connection module provides the building blocks to connect external data to language models. The modular design allows customizing pipelines for specific use cases.


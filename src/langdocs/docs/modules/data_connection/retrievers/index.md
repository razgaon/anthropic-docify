

# Retrievers

## Introduction

Retrievers allow finding relevant documents from a corpus for a given query. They are a key component in many natural language processing applications like question answering. This guide provides an overview of retrievers in LangChain and how to use them.

LangChain provides integration with several vector stores that can be used to build powerful retrievers. The default vector store is [Chroma](/docs/ecosystem/integrations/chroma.html), but others like FAISS are also supported.

## Vector Store-Backed Retrievers

A vector store retriever wraps a vector store index and provides a simple interface to retrieve documents relevant to a query. 

To create one, you first build the vector store index:

### Text Splitting

Documents are split into smaller chunks before indexing. For example:

```python
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000)  
texts = text_splitter.split_documents(documents)
```

LangChain supports splitting by characters, sentences, paragraphs, etc.

### Generating Embeddings 

Embeddings are generated for each text chunk to capture semantic meaning:

```python 
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
```

OpenAI Embeddings, SentenceTransformers etc. are supported.

### Indexing in Vector Store

Text chunks and embeddings are indexed in the vector store:

```python
from langchain.vectorstores import Chroma

index = Chroma.from_documents(texts, embeddings)
```

Chroma, FAISS, Weaviate etc. integrations are provided.

### Creating the Retriever 

The vector store is wrapped in a retriever:

```python
retriever = index.as_retriever() 
```

The retriever uses the vector store's similarity search to find relevant documents.

You can customize parameters like number of docs returned, search algorithm, etc.

## Using a Retriever for Question Answering

A common use case for retrievers is question answering:

1. Index documents
2. Create retriever
3. Create question answering chain 
4. Ask questions!

For example:

```python
# index documents
index = Chroma.from_documents(texts, embeddings)

# create retriever 
retriever = index.as_retriever()  

# load question answering chain
qa = RetrievalQA(retriever=retriever)

# ask question
qa.run("What did the president say about X?") 
```

The RetrievalQA chain allows specifying the QA logic used. For example:

```python 
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=retriever)
```

You can also directly pass in a custom QA chain for more control.

## Conclusion

Retrievers provide a simple way to find relevant documents from a corpus. LangChain makes it easy to build and customize vector store-backed retrievers using different text and embedding strategies. They are a key component in NLP applications like question answering.


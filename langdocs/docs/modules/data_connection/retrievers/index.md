

# Retrievers

## Introduction

Retrievers are a key component in many natural language processing systems. As mentioned in the FAQ, a retriever is an interface that returns documents given an unstructured query. It does not need to store documents, only return them. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well. This guide will provide an overview of retrievers in LangChain and walk through creating and using a retriever for question answering.

## Vector Store-Backed Retrievers

The main type of retriever in LangChain is backed by a vector store index. As mentioned in the FAQ, LangChain uses Chroma by default as the vector store. Vector stores like Chroma and FAISS allow you to index text embeddings for efficient similarity search.

For example, to create a vector store index with Chroma:

```python
from langchain.document_loaders import TextLoader  
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma  
from langchain.embeddings import OpenAIEmbeddings

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000)  
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(texts, embeddings) 
```

As mentioned in the FAQ, you can then easily wrap the vector store in a retriever:

```python
retriever = db.as_retriever()
```

The retriever will use the vector store's similarity search to find relevant documents.

You can also use other vector stores like FAISS:

```python
from langchain.vectorstores import FAISS

db = FAISS.from_documents(texts, embeddings)
retriever = db.as_retriever()
```

### Customizing Search

As shown in the FAQ, the vector store retriever provides options to customize the search method and parameters:

- `search_type` - Options like "similarity" (default), "mmr", "similarity_threshold"
- `search_kwargs` - Specify arguments like `k` for top k results

For example:

```python
retriever = db.as_retriever(
  search_type="mmr",  
  search_kwargs={"k": 5}   
)
```

## Using a Retriever for Question Answering

As mentioned in the FAQ, retrievers are commonly used for question answering. This is a good example because it combines multiple components like text splitting, embeddings, and vector stores. 

The question answering process consists of 4 main steps:

1. Create an index
2. Create a Retriever from that index 
3. Create a question answering chain
4. Ask questions!

You can pass a retriever to a `RetrievalQA` chain:

```python
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

qa = RetrievalQA(
  retriever=retriever,
  llm=OpenAI()   
)

qa.run("What did the president say about climate change?") 
```

The chain will use the retriever to find relevant documents, summarize them with the LLM, and produce an answer.

## Conclusion

In summary, retrievers provide a way to find relevant documents for a query. Vector store-backed retrievers allow efficient similarity search over indexed embeddings. Retriever configuration provides flexibility in customizing search methods and parameters. In LangChain, retrievers can be easily integrated into question answering and other natural language chains.


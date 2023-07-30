
Here is a revised markdown page improving on the reference documentation:

# Question Answering with LangChain

## Introduction

This document provides a guide to using LangChain for question answering over text documents. We will cover:

- Installing LangChain  
- Preparing data
- Quickstart usage
- Different chain types
- Customizing prompts
- Returning intermediate steps  
- Document QA with sources

## Requirements

To follow this guide, you will need:

- Python 3.7+
- LangChain library
- OpenAI API key

Install LangChain:

```
pip install langchain
```

## Prepare Data

We will do similarity search over text documents with a vector database backend. The documents can be fetched in any manner. 

Import required libraries:

```python
from langchain.embeddings.openai import OpenAIEmbeddings   
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.indexes.vectorstore import VectorstoreIndexCreator
```

Load document text and split into chunks:

```python  
with open("state_of_the_union.txt") as f:
 state_of_the_union = f.read()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
texts = text_splitter.split_text(state_of_the_union)
```

Encode chunks with OpenAI embeddings and index with Chroma:

```python
embeddings = OpenAIEmbeddings()

docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": str(i)} for i in range(len(texts))]).as_retriever() 

print("Running Chroma using direct local API.")
print("Using DuckDB in-memory for database. Data will be transient.")
```

Define a sample question:

```python 
query = "What did the president say about Justice Breyer"
docs = docsearch.get_relevant_documents(query)
```

## Quickstart

To quickly run QA over the prepared documents:

```python
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

query = "What did the president say about Justice Breyer"  
result = chain.run(input_documents=docs, question=query)

print(result)
```

This will run the `stuff` chain using OpenAI as the backend LLM and print the answer.

## Chain Types

LangChain provides different chain types for QA:

### `stuff` Chain

Uses a simple prompt to process documents and answer the question.

```python
chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
result = chain({"input_documents": docs, "question": query}, return_only_outputs=True) 
print(result)
```

### `map_reduce` Chain

Maps documents to summaries, then reduces to final answer.

```python  
chain = load_qa_chain(OpenAI(temperature=0), chain_type="map_reduce")
result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
print(result)
```

### `refine` Chain  

Iteratively refines answer using provided context.

```python
chain = load_qa_chain(OpenAI(temperature=0), chain_type="refine") 
result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)   
print(result)
```

### `map-rerank` Chain

Maps documents to QA pairs, then reranks to get best answer.

```python
chain = load_qa_chain(OpenAI(temperature=0), chain_type="map_rerank", return_intermediate_steps=True)
result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
print(result["output_text"])  
print(result["intermediate_steps"])
```

## Customizing Prompts

You can provide custom prompt templates:

```python
prompt_template = """  
{context}
Question: {question}
Answer: 
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff", prompt=prompt)
```

## Intermediate Steps  

For `map_reduce` and `refine` chains, you can return intermediate steps:

```python
chain = load_qa_chain(OpenAI(temperature=0), chain_type="refine", return_refine_steps=True)
result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)

print(result["intermediate_steps"]) 
```

## Document QA with Sources

To return document sources with the answer:

```python
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="stuff")   
result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)

print(result)  
```

## Summary

In this guide, we covered using LangChain for question answering over text documents. The key steps are:

- Installing requirements  
- Preparing and indexing data  
- Loading different QA chains
- Customizing prompts
- Accessing intermediate steps
- Getting document sources

LangChain provides a flexible framework for QA using LLMs like OpenAI.


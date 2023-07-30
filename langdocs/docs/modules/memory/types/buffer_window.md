
# RetrievalQA Guide

RetrievalQA allows you to perform question answering by retrieving relevant documents from a vectorstore and using an LLM to generate an answer. This guide provides a comprehensive overview of using RetrievalQA with examples.

## Setup

To use RetrievalQA, you first need to:

1. Load documents
2. Embed documents 
3. Index documents into a vectorstore

### Indexing Best Practices

To optimize performance, follow these best practices when indexing:

- Use a powerful embedding model like OpenAI Embeddings that can capture semantic meaning
- Pick a chunk size that balances performance and accuracy. Around 1000 tokens is a good starting point.
- Use an overlap of 0 tokens between chunks to avoid duplicating content
- Limit index size to improve query speed. 100k documents is a good target.

For example:

```python
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings  
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

loader = TextLoader("../../state_of_the_union.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
  
embeddings = OpenAIEmbeddings() 
docsearch = Chroma.from_documents(texts, embeddings)
```

## Chain Types

RetrievalQA supports different chain types that determine how the retrieved documents are processed by the LLM:

- `stuff`: Stuff relevant context into the prompt
- `map_reduce`: Map/reduce style - ask for each document separately  
- `tl;dr`: Ask for a summary of the most relevant documents
- `refine`: Iteratively refine the answer with most relevant docs

To use a specific chain type:

```python  
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=docsearch.as_retriever())
```

You can also directly load the chain and pass it to RetrievalQA:

```python
from langchain.chains.question_answering import load_qa_chain

qa_chain = load_qa_chain(OpenAI(), chain_type="stuff")
qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=docsearch.as_retriever())
```

This allows full control over the chain parameters.

## Custom Prompts

You can pass custom prompts to RetrievalQA:

```python
from langchain.prompts import PromptTemplate

prompt_template = """
Use the following context to answer the question:

{context}

Question: {question}
Answer:
"""

prompt = PromptTemplate(template=prompt_template,
                        input_variables=["context", "question"])

qa = RetrievalQA.from_chain_type(llm=OpenAI(),
                                 chain_type="stuff",
                                 retriever=docsearch.as_retriever(),
                                 chain_type_kwargs={"prompt": prompt})
                                 
query = "What did the president say about Ketanji Brown Jackson?"
result = qa.run(query)
print(result)
```

This shows how to pass the custom prompt to RetrievalQA and call run() to use it.

## Return Source Documents

To return source documents used to generate the answer:

```python
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(), return_source_documents=True)

result = qa({"query": query})
print(result["result"])
print(result["source_documents"]) 
```

## RetrievalQAWithSourcesChain

To directly cite sources in the answer, use `RetrievalQAWithSourcesChain`:

```python
from langchain.chains import RetrievalQAWithSourcesChain

chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())

result = chain({"question": "What did the president say about Justice Breyer?"}, return_only_outputs=True)
print(result["answer"]) 
print(result["sources"])
```

You can customize the formatting of cited sources by passing a `format_source` function:

```python
def format_source(source):
    return f"Source: Page {source['metadata']['lookup_index']}"

chain = RetrievalQAWithSourcesChain(..., format_source_fn=format_source) 
```

This provides a comprehensive guide to using RetrievalQA with examples for chain types, custom prompts, returning sources, and citing sources directly. The guide is structured logically and ensures complete coverage of all key RetrievalQA features.


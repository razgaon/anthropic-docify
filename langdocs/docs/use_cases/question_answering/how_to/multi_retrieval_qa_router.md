

# Dynamically select from multiple retrievers

This notebook demonstrates how to use the `MultiRetrievalQAChain` to dynamically select which retrieval system to use for answering a question. The `MultiRetrievalQAChain` takes in a list of `retriever_infos` dicts that each specify a name, description, and retriever. It selects the best matching retriever for a given question.

## Setup

Here is some sample code for loading documents into FAISS indexes and wrapping them as retrievers:

```python
sou_docs = TextLoader('../../state_of_the_union.txt').load_and_split()
sou_retriever = FAISS.from_documents(sou_docs, OpenAIEmbeddings()).as_retriever()

pg_docs = TextLoader('../../paul_graham_essay.txt').load_and_split()  
pg_retriever = FAISS.from_documents(pg_docs, OpenAIEmbeddings()).as_retriever()
```

We then create a list of `retriever_infos` dicts that specify a name, description, and the retriever:

```python
retriever_infos = [
  {
    "name": "state of the union",
    "description": "Good for answering questions about the 2023 State of the Union address",    
    "retriever": sou_retriever
  },
  {
    "name": "pg essay",
    "description": "Good for answering questions about Paul Graham's essay on his career",
    "retriever": pg_retriever
  }
]
```

## Creating the MultiRetrievalQAChain

We can now create the `MultiRetrievalQAChain` by passing the list of retriever infos:

```python
chain = MultiRetrievalQAChain.from_retrievers(OpenAI(), retriever_infos, verbose=True)
```

The `verbose=True` will print out which retriever was selected for each question.

## Customizing Prompts

You can customize the prompts used for question answering by passing a `PromptTemplate` to the `MultiRetrievalQAChain`. 

For example:

```python
from langchain.prompts import PromptTemplate

prompt_template = """Use the following context to answer the question in Italian:

{context}

Domanda: {question}
Risposta:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain = MultiRetrievalQAChain.from_retrievers(OpenAI(), retriever_infos, prompt=prompt)
```

## Return Source Documents

We can also return the source documents used to generate the answer by passing `return_source_documents=True`:

```python
chain = MultiRetrievalQAChain.from_retrievers(OpenAI(), retriever_infos, return_source_documents=True)
```

This allows accessing the provenance for an answer.

In summary, the `MultiRetrievalQAChain` provides a way to dynamically select between multiple retrievers based on the question. By configuring multiple retrievers, we can build QA systems that combine domain-specific and personal knowledge.


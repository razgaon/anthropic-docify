

# QA using a Retriever

This example showcases question answering over an index.

## Overview

The RetrievalQA chain allows performing question answering by first retrieving relevant documents from an index using a retriever, and then generating an answer using those documents. It provides flexibility to:

- Use different chain types for answer generation like "stuff" or "reduce" 
- Customize prompts for question answering
- Return source documents used to generate the answer
- Cite sources by passing document metadata

## Usage

To use RetrievalQA:

1. Index documents using a retriever like Chroma
2. Instantiate RetrievalQA chain with retriever 
3. Customize chain type, prompts etc.
4. Pass a question query to the chain

It will retrieve relevant documents and generate an answer.

## Customizing Behavior

### Chain Types

You can specify different chain types like "stuff" or "map_reduce" when creating the chain:

```python
qa = RetrievalQA.from_chain_type(
  llm=OpenAI(),
  chain_type="map_reduce", 
  retriever=docsearch.as_retriever()
)
```

Or load the chain directly and pass it:

```python
from langchain.chains.question_answering import load_qa_chain
qa_chain = load_qa_chain(llm, "reduce")
qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=docsearch.as_retriever())
```

### Custom Prompts

You can pass custom prompts to RetrievalQA:

```python 
prompt_template = """
{context}
Question: {question}
Answer in Italian:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

qa = RetrievalQA.from_chain_type(
  llm=OpenAI(),
  chain_type="stuff",
  prompt=prompt,
  retriever=docsearch.as_retriever()  
)
```

### Returning Source Documents

You can return source documents used to generate the answer:

```python
qa = RetrievalQA.from_chain_type(
  llm=OpenAI(),
  chain_type="stuff",
  retriever=docsearch.as_retriever(),
  return_source_documents=True  
)

result = qa.run(query)
answer = result["result"]
sources = result["source_documents"]
```

### Citing Sources 

If documents have a "source" metadata key, you can use `RetrievalQAWithSourcesChain` to cite sources:

```python
docsearch = Chroma.from_texts(
  texts, 
  embeddings,
  metadatas=[{"source": f"{i}-src"}]
)

from langchain.chains import RetrievalQAWithSourcesChain

chain = RetrievalQAWithSourcesChain.from_chain_type(
  llm=OpenAI(),
  chain_type="stuff",
  retriever=docsearch.as_retriever()
)

result = chain.run(query) 
# Answer contains citations
```

## Conclusion

The RetrievalQA chain provides a flexible way to perform question answering over documents using LangChain. It supports customizing chain types, prompts and output to enable diverse question answering workflows.

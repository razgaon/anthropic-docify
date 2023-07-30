

# Using RetrievalQA for Question Answering

## Overview

The RetrievalQA chain allows performing question answering by first retrieving relevant documents from an index, and then generating an answer using those documents. This guide covers key concepts and provides comprehensive examples for customizing and using RetrievalQA effectively in practice.

## Loading Chain Types

RetrievalQA supports different underlying question answering chains that operate on the retrieved documents. These are called chain types and determine the question answering approach. 

Some common chain types include:

- `stuff`: Generates an answer with no intermediate steps shown. Useful for simple fact-based QA.

- `map_reduce`: Shows intermediate summarization steps. Useful for more complex questions that require summarizing evidence. 

- `refine`: Iteratively refines the answer. Useful for questions where the initial answer needs improvement.

You can load a chain type when constructing the RetrievalQA chain:

```python
qa = RetrievalQA.from_chain_type(llm=OpenAI(), 
                                 chain_type="map_reduce", 
                                 retriever=docsearch.as_retriever())
```

Alternatively, you can load the QA chain directly and pass it to RetrievalQA. This allows full control over the chain parameters:

```python
from langchain.chains.question_answering import load_qa_chain

qa_chain = load_qa_chain(llm=OpenAI(), chain_type="stuff")

qa = RetrievalQA(combine_documents_chain=qa_chain, 
                 retriever=docsearch.as_retriever())
```

## Customizing Prompts

You can customize the prompts used for question answering in RetrievalQA. For example, this prompt template answers questions in Italian:

```python
from langchain.prompts import PromptTemplate

prompt_template = """
{context}
Question: {question}
Answer in Italian:
"""

prompt = PromptTemplate(template=prompt_template,
                        input_variables=["context", "question"]) 

qa = RetrievalQA.from_chain_type(llm=OpenAI(),
                                 prompt=prompt, 
                                 retriever=docsearch.as_retriever())
```

Prompts can be tailored to your specific use case or domain. See the [question answering notebook](https://langchain.readthedocs.io/en/latest/modules/chains/additional/question_answering.html) for more examples.

## Returning Source Documents

To return the source documents used to generate the answer:

```python
qa = RetrievalQA.from_chain_type(llm=OpenAI(),
                                 return_source_documents=True, 
                                 retriever=docsearch.as_retriever())
```

This adds a `source_documents` key to the results containing the sources.

## Citing Sources with RetrievalQAWithSourcesChain

To directly cite sources used to answer the question:

```python
from langchain.chains import RetrievalQAWithSourcesChain

chain = RetrievalQAWithSourcesChain.from_chain_type(llm=OpenAI(),
                                                    retriever=docsearch.as_retriever())

result = chain({"question": "What did the president say about Justice Breyer"})
print(result['sources'])
# Prints cited source key(s) 
```

The `RetrievalQAWithSourcesChain` returns the cited source keys directly.

## Conclusion

In summary, RetrievalQA provides a flexible question answering interface using retrievers and underlying QA chains. Key features include loading chain types, customizing prompts, returning source documents, and citing sources directly. This guide covered comprehensive examples to help customize RetrievalQA for your use case.


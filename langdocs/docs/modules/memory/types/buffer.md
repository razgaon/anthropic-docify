

# RetrievalQA

## Overview

The RetrievalQA chain has two main components:

1. **Retriever**: Indexes and searches over a set of documents to find relevant passages for a question. Can be a vector store like Chroma or Anserini.

2. **Question Answering Model**: Reads the identified relevant passages and generates an answer to the question. Typically a large language model like GPT-3. 

To use RetrievalQA:

1. Index your documents into a retriever.

2. Initialize the chain by passing the retriever. 

3. Call `run()` with your question.

Under the hood, RetrievalQA will use the retriever to find relevant documents, run them through the QA model to generate an answer.

## Chain Types

You can specify different chain types that define the question answering prompt/logic used by the QA model. For a detailed overview, see [this notebook](/docs/modules/chains/additional/question_answering.html).

The main ways to configure chain types are:

- Set `chain_type` in `from_chain_type()`: Simplest option, just pass the name like "reduce_concat" or "stuff.p0".

- Load with `load_qa_chain()` and pass to `combine_documents_chain`: More control over parameters but more complex.

## Custom Prompts

You can customize the prompt used for question answering by passing a `PromptTemplate` to RetrievalQA. The prompts can use variables like `{context}` and `{question}` that will be populated dynamically with the retrieved documents and input question.

For example:

```python
from langchain.prompts import PromptTemplate

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.  

{context}

Question: {question}
Answer:"""

prompt = PromptTemplate(template=prompt_template, 
                        input_variables=["context", "question"])
```

See the [question answering notebook](/docs/modules/chains/additional/question_answering.html) for more details on constructing prompt templates.

## Return Source Documents

You can return the source documents used to generate the answer by passing `return_source_documents=True` when initializing the chain. This will return a dict with the `"answer"` and `"source_documents"`.

## Example Usage

```python
from langchain import OpenAI, RetrievalQA

docs = [...] # list of Document objects
embeddings = OpenAIEmbeddings()
retriever = Chroma.from_documents(docs, embeddings) 

qa = RetrievalQA(OpenAI(), retriever)

qa.run("What is LangChain used for?") 
```

This initializes the chain with GPT-3 as the QA model and a Chroma index over the documents. `run()` will then find relevant docs and extract the answer.


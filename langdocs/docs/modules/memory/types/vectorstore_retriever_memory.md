

# RetrievalQA

## Overview

RetrievalQA is a chain in LangChain for doing question answering by first retrieving relevant documents from a vectorstore and then using those documents to generate an answer. 

To use RetrievalQA:

1. Load documents into a vectorstore
2. Initialize the chain by passing the vectorstore 
3. Call `run()` with a question to get the answer

## Usage

First load documents and index them into a vectorstore:

```python
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings   
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

loader = TextLoader("documents.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()  
docsearch = Chroma.from_documents(texts, embeddings)
```

Then initialize the RetrievalQA chain by passing the vectorstore:

```python
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())
```

Finally, ask a question to get the answer:

```python
query = "What did the president say about Ketanji Brown Jackson?"
result = qa.run(query)
print(result)
```

## Chain Types

RetrievalQA supports different underlying question answering chains through the `chain_type` parameter:

- `stuff`: Uses a basic prompt with extracted context.
- `map_reduce`: Maps questions to answers independently per document.  
- `refine`: Iteratively refines an answer using extracted context.

For example, to use the `refine` chain:

```python
from langchain.chains.question_answering import load_qa_chain

qa_chain = load_qa_chain(llm=OpenAI(), chain_type="refine")
qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=docsearch.as_retriever()) 
```

## Custom Prompts

You can pass custom prompts to RetrievalQA:

```python
from langchain.prompts import PromptTemplate

prompt_template = """  
{context}
Question: {question}
Answer:
"""

prompt = PromptTemplate(template=prompt_template,
                        input_variables=["context", "question"])

qa = RetrievalQA.from_chain_type(
   llm=OpenAI(),
   chain_type="stuff",
   retriever=docsearch.as_retriever(),
   chain_type_kwargs={"prompt": prompt}
)
```

## Returning Source Documents 

To return the source documents used by RetrievalQA:

```python
qa = RetrievalQA.from_chain_type(
   llm=OpenAI(),
   chain_type="stuff",
   retriever=docsearch.as_retriever(),  
   return_source_documents=True
)

result = qa.run("What did the president say about Ketanji Brown Jackson?")
print(result["result"])  
print(result["source_documents"])
```

You can also use the `RetrievalQAWithSourcesChain` to directly return sources cited:

```python
from langchain.chains import RetrievalQAWithSourcesChain

chain = RetrievalQAWithSourcesChain.from_chain_type(
    OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever()  
)

result = chain.run("What did the president say about Ketanji Brown Jackson?") 
print(result["answer"])
print(result["sources"])
```


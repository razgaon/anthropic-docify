

# Using RetrievalQA in LangChain

## Introduction

The `RetrievalQA` chain in LangChain allows you to perform question answering by retrieving relevant documents from an index and using them to generate an answer. This guide will provide an overview of `RetrievalQA` and examples of how to use it effectively.

## Preprocessing Documents

Before loading documents into RetrievalQA, it is important to clean and preprocess them. This can involve steps like:

- Removing HTML tags, scripts, etc.
- Normalizing whitespace
- Lowercasing 
- Removing stop words
- Lemmatizing words

This helps improve the quality of document embeddings and retrieval.

## Loading and Indexing Documents

To use `RetrievalQA`, you first need to load documents into memory and index them. You can load documents using the `TextLoader` and split them using the `CharacterTextSplitter`:

```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

loader = TextLoader("data.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000)  
texts = text_splitter.split_documents(documents)
```

Once you have documents loaded and split, you need to index them for efficient retrieval. You can use Chroma to index texts and convert them into a retriever:

```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_texts(texts, embeddings)

retriever = docsearch.as_retriever()
```

## Using RetrievalQA

With a retriever loaded, you can now construct a `RetrievalQA` chain to run queries:

```python
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

qa = RetrievalQA(llm=OpenAI(), retriever=retriever)

query = "What is LangChain used for?"
result = qa.run(query)
```

This will retrieve relevant documents and use them to generate an answer to the question.

## Chain Types

You can specify different underlying question answering chains in `RetrievalQA` using the `chain_type` parameter:

```python
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=retriever)
```

Some common options are "reduce", "map_reduce", "stuff", and "refine". See the [question answering guide](https://langchain.readthedocs.io/en/latest/modules/chains/additional/question_answering.html) for details on the different chain types.

## Custom Prompts

You can provide custom prompts to `RetrievalQA` to customize the question answering behavior. For example:

```python
from langchain.prompts import PromptTemplate

prompt_template = """
{context}
Question: {question}
Answer:
"""

prompt = PromptTemplate(template=prompt_template,
                        input_variables=["context", "question"])

qa = RetrievalQA(prompt=prompt, llm=OpenAI(), retriever=retriever)
```

The prompt can include conditional logic, answer formatting, and other customizations.

## Returning Source Documents 

To return source documents used to generate the answer, set `return_source_documents=True`:

```python
qa = RetrievalQA(llm=OpenAI(),  
                 retriever=retriever,
                 return_source_documents=True)

result = qa.run("What does the text say about pandas?")

print(result["source_documents"]) # Documents used
```

You can also use the `RetrievalQAWithSourcesChain` to directly return sources:

```python
from langchain.chains import RetrievalQAWithSourcesChain

chain = RetrievalQAWithSourcesChain(llm=OpenAI(), retriever=retriever)
result = chain.run("What does the text say about pandas?")

print(result["sources"]) # Sources cited
```

## Troubleshooting

Here are some common issues and solutions when using RetrievalQA:

- **No relevant documents returned** - Try expanding the document collection, using better document embeddings, or reformulating the query.

- **Irrelevant documents returned** - Try cleaning documents more thoroughly, tuning the retriever, or using a different chain type.

- **Inaccurate or incomplete answers** - Try using a different LLM, chain type, or prompt structure.

- **Slow performance** - Reduce number of documents indexed, use approximate nearest neighbor retrieval, or lower the chunk size.

## Conclusion

In summary, `RetrievalQA` provides a flexible framework for question answering using retrievers and LLMs in LangChain. With proper setup and tuning, it enables powerful QA over large document collections.


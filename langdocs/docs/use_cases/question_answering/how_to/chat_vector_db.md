

# Store and reference chat history

The ConversationalRetrievalQA chain in LangChain builds on the RetrievalQAChain to provide a chat history component for conversational question answering.

## Overview

The ConversationalRetrievalQA chain works by combining the chat history and current question into a standalone question string. It uses this to retrieve relevant documents, then passes those documents and original question to a QA chain to generate a response. 

Some key advantages:

- Allows stateful conversational QA 
- Leverages chat history for consistency and context

## Usage

To create a ConversationalRetrievalQA chain, you first need a retriever. You can create one from a vector store built with embeddings:

```python
from langchain.embeddings.openai import OpenAIEmbeddings  
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings) 
```

You also need a memory object to track chat history across questions:

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
```

Then initialize the chain:

```python 
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI

qa = ConversationalRetrievalChain.from_llm(
    OpenAI(temperature=0),
    vectorstore.as_retriever(),
    memory=memory
)
```

You can now ask a question, get the answer, and ask a followup using the stored history:

```python
query = "What did the president say about Ketanji Brown Jackson"
result = qa({"question": query}) 

chat_history = [(query, result["answer"])]
query = "Did he mention who she succeeded"
result = qa({"question": query, "chat_history": chat_history})

print(result['answer']) 
```

## Customizing Chat History

You can customize how chat history is formatted by providing a `get_chat_history` function:

```python
def get_chat_history(inputs):
  # Format inputs however you want
  return formatted_history 

qa = ConversationalRetrievalChain(..., get_chat_history=get_chat_history)
```

## Hyperparameter Tuning

Important hyperparameters like `search_distance` can be set on the vectorstore: 

```python
vectorstore = Chroma(..., search_distance=0.8) 
```

## Conclusion

The ConversationalRetrievalQA chain enables stateful conversational QA by storing chat history. It provides flexibility to customize chat history formatting and tune hyperparameters.


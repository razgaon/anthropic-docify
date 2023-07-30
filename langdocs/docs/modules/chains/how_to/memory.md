

# Adding Memory to Chains

## Introduction

Chains in LangChain can be made stateful by initializing them with a Memory object. This allows data to persist across multiple calls to the chain. The Memory module in LangChain provides various utilities for adding memory to chains.

## Get Started

To get started with memory, you can initialize a chain like ConversationChain with a Memory object:

```python
from langchain.chains import ConversationChain  
from langchain.memory import ConversationBufferMemory
  
conversation = ConversationChain(
  llm=chat,
  memory=ConversationBufferMemory()  
)
```

This will store the conversation history in the Memory object and make it available across runs of the chain.

## ConversationBufferMemory

One simple memory type is ConversationBufferMemory. This keeps a buffer of the full conversation history. For example:

```python
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("hi!") 
memory.chat_memory.add_ai_message("hello!")
```

The full buffer is then available to inject into prompts.

## ConversationSummaryMemory

For longer conversations, ConversationSummaryMemory can be used to store a summary instead of the full history. This summarizes the conversation on the fly using an LLM.

For example:

```python 
memory = ConversationSummaryMemory(llm=GPT3)
# Messages get summarized
memory.save_context(...) 

# Summary returned 
memory.load_memory_variables({})
```

You can also initialize the memory directly from existing messages:

```python
history = ChatMessageHistory()
# Add messages
memory = ConversationSummaryMemory.from_messages(llm, history) 
```

## Conclusion

The LangChain Memory modules make it easy to add stateful memory to chains. Developers can leverage different storage options like buffering or summarization depending on their needs.


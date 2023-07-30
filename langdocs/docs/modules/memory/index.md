

# Memory

## Overview

Memory is critical for conversational context in AI systems built with LangChain. It allows the system to maintain state across interactions by reading from and writing to a persistent storage. 

At minimum, memory needs to store a history of chat interactions. More advanced systems build indexes, summaries or knowledge graphs on top of history to provide targeted context.

LangChain provides tools for incorporating memory ranging from simple buffers to complex knowledge graphs. Memory can be integrated into chains and models with just a few lines of code.

## Building Memory into a System

There are two key design decisions when building memory:

### Storing: List of Chat Messages

The underlying storage needs to be a list of chat messages, even if not all are directly used. LangChain offers integrations for in-memory storage or persistent databases to store this history.

[Chat message storage](/docs/modules/memory/chat_messages) covers the available storage options.

### Querying: Data Structures and Algorithms 

On top of raw message storage, data structures and algorithms are needed to query messages. Simple systems may return recent messages verbatim. More advanced ones build indexes or summaries to provide targeted context. 

LangChain supports [various memory types](/docs/modules/memory/types) from simple buffers to knowledge graphs.

## Usage

Memory is used by passing a `Memory` object when initializing a chain:

```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
conversation = ConversationChain(
   memory=memory
) 
```

The memory will automatically be read before each call and written to after. See the [examples](/docs/examples/memory) for more end-to-end usage.

When implementing custom memory, key concepts include controlling returned memory variables, returning messages as strings vs lists, and specifying input/outputs to store.

## Summary

Memory provides conversational context critical for natural dialogs. LangChain offers tools ranging from simple buffers to complex knowledge graphs. Memory integrates seamlessly into chains and models with just a few lines of code.


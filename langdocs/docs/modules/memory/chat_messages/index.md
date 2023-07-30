

# Chat Messages

## Overview

The `ChatMessageHistory` class provides a lightweight way to store a history of chat messages between a human and an AI agent. It can be useful both when managing memory directly or when integrated into an LLMChain or ChatModelChain. 

## Usage

To use `ChatMessageHistory`:

```python
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

history.add_user_message("Hi there!") 
history.add_ai_message("Hello! Nice to meet you.")
```

The `add_user_message` and `add_ai_message` methods allow you to append new messages to the history. 

You can then access the full message history:

```python
history.messages
```

Which would return:

```
[
  HumanMessage(content='Hi there!'),
  AIMessage(content='Hello! Nice to meet you.')  
]
```

## Advanced Usage

The `ChatMessageHistory` supports some more advanced usage:

- **Metadata**: You can pass additional metadata like `username` when adding messages:

  ```python
  history.add_user_message("Hi there!", username="john")
  ```

- **Custom message types**: You can subclass `ChatMessage` to create custom message types:

  ```python
  class SystemMessage(ChatMessage):
      pass

  history.add_message(SystemMessage("Loading..."))
  ```

- **Serialization**: `ChatMessageHistory` can be serialized to JSON for persistence:

  ```python
  json_string = history.to_json()
  new_history = ChatMessageHistory.from_json(json_string)
  ```

## Using in Chains

`ChatMessageHistory` can be used in chains by passing it to the `memory` parameter:

```python
from langchain.chains import LLMChain

memory = ChatMessageHistory()
chain = LLMChain(..., memory=memory)
```

The chain will automatically read/write messages to the history.

One of the core utility classes underpinning most (if not all) memory modules is the ChatMessageHistory class. This is a super lightweight wrapper which exposes convenience methods for saving Human messages, AI messages, and then fetching them all.

You may want to use this class directly if you are managing memory outside of a chain.

Let's take a look at using this in a chain. We'll use an LLMChain, and show working with both an LLM and a ChatModel.

#### Using an LLM

Notice that 'chat_history' is present in the prompt template. Notice that we need to align the memory_key.

#### Using a ChatModel

Notice that we return_messages=True to fit into the MessagesPlaceholder. Notice that "chat_history" aligns with the MessagesPlaceholder name.

### Next Steps

Please see the other sections for walkthroughs of more advanced topics, like custom memory, multiple memories, and more.

## Memory Concepts

When using memory in a chain, there are a few key concepts to understand. Note that here we cover general concepts that are useful for most types of memory. Each individual memory type may very well have its own parameters and concepts that are necessary to understand.

### What variables get returned from memory

Before going into the chain, various variables are read from memory. This have specific names which need to align with the variables the chain expects. You can see what these variables are by calling `memory.load_memory_variables({})`. Note that the empty dictionary that we pass in is just a placeholder for real variables. If the memory type you are using is dependent upon the input variables, you may need to pass some in.

### Whether memory is a string or a list of messages

One of the most common types of memory involves returning a list of chat messages. These can either be returned as a single string, all concatenated together (useful when they will be passed in LLMs) or a list of ChatMessages (useful when passed into ChatModels). By default, they are returned as a single string. In order to return as a list of messages, you can set `return_messages=True`

### What keys are saved to memory

Often times chains take in or return multiple input/output keys. In these cases, how can we know which keys we want to save to the chat message history? This is generally controllable by `input_key` and `output_key` parameters on the memory types. These default to None - and if there is only one input/output key it is known to just use that. However, if there are multiple input/output keys then you MUST specify the name of which one to use.


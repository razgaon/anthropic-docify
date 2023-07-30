
# Conversation Buffer Memory

## Overview

The `ConversationBufferMemory` class in LangChain allows storing chat messages from a conversation and extracting them into a variable that can be injected into a prompt or model. This enables maintaining context over the course of a conversation.

There are two main ways to extract the chat history:

- As a single string containing the concatenated messages
- As a list of `ChatMessage` objects  

The class has configurable parameters to control:

- The memory key name returned
- Whether messages are returned as strings or list
- Which input and output keys are saved

## Usage

To use `ConversationBufferMemory`, first import and instantiate the class:

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
```

Then you can add chat messages from the user and AI:

```python
memory.chat_memory.add_user_message("Hi there!")
memory.chat_memory.add_ai_message("Hello!") 
```

To return the chat history as a single concatenated string:

```python
memory.load_memory_variables({})

{'history': 'Human: Hi there!\nAI: Hello!'}
```

To return the chat history as a list of `ChatMessage` objects:

```python  
memory = ConversationBufferMemory(return_messages=True)

memory.load_memory_variables({})

{'history': [HumanMessage(content='Hi there!'),  
             AIMessage(content='Hello!')]}
```

## Customizing Memory Keys

You can customize the memory key returned, as well as the input and output keys saved:

```python
# Change memory key
memory = ConversationBufferMemory(memory_key="chat_history")

# Change input key  
memory = ConversationBufferMemory(input_key="user_input")

# Change output key
memory = ConversationBufferMemory(output_key="bot_response")
```

## Memory Size Management

Since all messages are stored, the memory can grow very large. Some ways to manage the size:

- Set a maximum number of messages with `max_messages`
- Use a sliding window approach like `ConversationBufferWindowMemory` 
- Periodically clear old messages with `chat_memory.clear()`

## Examples

See the [memory examples](https://github.com/Anthropic/langchain/tree/main/examples/memory) for more usage details.

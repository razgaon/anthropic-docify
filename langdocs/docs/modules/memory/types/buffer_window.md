

# Conversation Buffer Window Memory

`ConversationBufferWindowMemory` keeps a sliding window of the most recent K interactions in a conversation. This can be useful for limiting the memory size, rather than storing the full history.

## Usage

Let's explore the basics of using this memory type.

First we initialize the memory, setting the window size k. The default is k=10.

```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=5)  
```

We can then save chat messages to the memory. This adds them to the buffer.

```python
memory.save_context({"input": "Hello"}, {"output": "Hi there!"})
```

To load the memory, we call `load_memory_variables`. This will return the most recent k messages.

```python
memory.load_memory_variables({})
```

```
{'history': 'Human: Hello\nAI: Hi there!'}
```

We can also return the messages as a list by setting `return_messages=True`.

```python
memory = ConversationBufferWindowMemory(k=5, return_messages=True)

memory.load_memory_variables({})
```

``` 
{'history': [HumanMessage(content='Hello'), AIMessage(content='Hi there!')]}
```

## Edge Case Behavior

If k is set higher than the current length of the message history, `load_memory_variables` will return the full history rather than truncating.

For example:

```python
memory = ConversationBufferWindowMemory(k=10)

memory.save_context({"input": "Hi"}, {"output": "Hello!"}) 

memory.load_memory_variables({})
```

This will return:

```
{'history': 'Human: Hi\nAI: Hello!'}
```

Rather than truncating since k > number of messages.

## Initializing from Existing Messages

Rather than saving messages within the chain, we can initialize the memory directly from a `ChatMessageHistory`.

```python
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()
history.add_user_message("Hello")  
history.add_ai_message("Hi there!")

memory = ConversationBufferWindowMemory.from_messages(chat_memory=history)
```

Now when we load variables, it will include the initialized messages.

## Using in a Chain

Let's look at using this memory type in a conversation chain.

We'll initialize the memory and chain:

```python
from langchain.llms import OpenAI
from langchain.chains import ConversationChain

memory = ConversationBufferWindowMemory(k=2)
chain = ConversationChain(
   llm=OpenAI(),
   memory=memory
)
```

Now when we call `predict`, the prompt will be augmented with the messages saved to memory.

```python 
chain.predict(input="Hello")

chain.predict(input="How are you?") 
```

The second prediction's prompt will contain the previous message history based on the window k:

```
Human: How are you?
AI: I'm doing great, thanks for asking!
```

## Summary

The key points of `ConversationBufferWindowMemory` are:

- It maintains a sliding window of the most recent k messages
- k controls how much history is retained  
- Can be initialized from existing ChatMessageHistory
- Works seamlessly in conversation chains
- If k is higher than current history, full history is returned


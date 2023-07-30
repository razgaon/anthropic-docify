

# Memory in LangChain

## Introduction

LangChain provides a variety of memory types to store conversation context and enable your AI assistant to reference past interactions. This guide covers key concepts applicable across memory types and provides examples for working with different memory types.

## Key Concepts

Before using specific memory types, it's helpful to understand these core ideas:

### Memory Keys

Most memory types allow specifying a `memory_key` parameter that controls the key name returned by `load_memory_variables()`. For example:

```python
memory = ConversationBufferMemory(memory_key="chat_history")
print(memory.load_memory_variables({}))  
# Returns: {'chat_history': 'Human: Hi there!'}
```

### Input Keys vs Output Keys 

When saving context, most types take `input` and `output` dicts. By default, full dicts are saved. To control which keys are saved, use `input_key` and `output_key` parameters.

For example:

```python
memory = ConversationBufferMemory(
   input_key="question",
   output_key="response"
)
# Only specified keys will be saved
```

### Returning Messages vs String

Some types return chat history as a string. To return a list of `ChatMessage` objects instead, set `return_messages=True`.

## Memory Types

### ConversationBufferMemory

Keeps a buffer of chat messages. Simplest memory type.

```python
memory = ConversationBufferMemory()

# Add messages  
memory.add_user_message("Hi there!")
memory.add_ai_message("Hello!") 

print(memory.load_memory_variables({}))
# Returns string by default 
# {'history': 'Human: Hi there!\nAI: Hello!'}

# Return list of ChatMessages
memory = ConversationBufferMemory(return_messages=True)
print(memory.load_memory_variables({})) 
# {'history': [UserMessage(...), AIMessage(...)]}
```

### EntityMemory

Extracts and stores entities from chat history.

```python
memory = EntityMemory()

# Entities will be extracted and stored
memory.add_user_message("My favorite food is pizza")
memory.add_ai_message("Pizza is delicious!") 

print(memory.entity_store.store) 
# {'favorite food': 'pizza'}
```

### KeyValueMemory

Stores key-value pairs explicitly set by user.

```python
memory = KeyValueMemory()

# Explicitly store key-value 
memory.set("name", "John")   

print(memory.kv_store.store)
# {'name': 'John'}
```

## Conclusion

This covers some key memory types in LangChain. See the [full list](/docs/modules/memory/types) for more. Memory is essential for conversational AI to reference past interactions. LangChain provides tools to quickly incorporate different memory types into your assistants.


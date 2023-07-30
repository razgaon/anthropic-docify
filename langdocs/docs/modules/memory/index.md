

# Memory

Conversational AI systems need memory - the ability to track context from previous interactions. As mentioned in the reference, memory is essential for natural conversations, as humans continuously refer back to earlier parts of a dialogue. At a minimum, AI systems require access to recent messages to maintain context. More advanced systems can maintain persistent knowledge about entities and relationships mentioned throughout the conversation.

LangChain provides various utilities for incorporating memory into conversational models. These memory tools can be used independently or integrated directly into chains and prompts. 

## Why Memory Matters

Memory is a key requirement for natural, coherent conversations. Without tracking context, an AI system would be unable to follow references or recall facts from earlier in the dialogue. Humans have extremely robust memory capacity, so providing AI systems with memory is essential for approaching human-level performance.

At a minimum, conversational AI systems need access to recent messages to maintain basic cohesion. More sophisticated systems can build persistent memory of entities, relationships, facts and other knowledge that is accumulated throughout the conversation.

LangChain provides flexible building blocks for adding different types of memory to conversational models. The memory utilities can be used independently or incorporated into prompt and chain designs.

## Memory System Architecture

As mentioned in the reference, every memory system involves two key design decisions:

**Storage:** How conversation history is stored - in memory, databases, etc. LangChain provides integrations for various storage options.

**Querying:** How relevant context is retrieved from storage. This ranges from returning recent messages to querying for entities.

LangChain aims to make it easy to start with simple memory techniques like buffers and build more advanced, custom systems as needed.

## Getting Started with Memory

Let's look at a simple memory example using `ConversationBufferMemory` which stores messages in a buffer and inserts them into prompts:

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.add_user_message("hi!")
memory.add_ai_message("hello!")  
```

As noted in the reference, key concepts when working with LangChain memory include:

**Returned Variables:** Memory returns variables that must match chain input names. Control this with `memory.load_memory_variables()`.

**Message Format:** Messages can be strings or lists. Set `return_messages=True` for list format.

**Saved Keys:** Specify inputs/outputs to save with `input_key` and `output_key` parameters.

See the examples below for end-to-end usage in chains.

## Custom Memory Types

As noted in the feedback, more guidance is needed on implementing custom memory classes. 

The core functionality of any memory class includes:

- `save_context` to save input/output context
- `load_memory_variables` to return memory variables

Additionally, custom memories may override: 

- `reset` to clear memory
- `close` for any cleanup logic

For example, here is a simple custom memory that saves a dictionary and returns it:

```python
class MyMemory:

  def __init__(self):
    self.memory = {}
  
  def save_context(self, input, output):
    self.memory.update(input)
    self.memory.update(output)

  def load_memory_variables(self, inputs):
    return self.memory
```

This could be integrated into a chain:

```python
memory = MyMemory()
chain = MyChain(memory=memory) 

chain.predict({"name": "John"})
# Memory now contains {"name": "John"}

print(memory.memory)
# {"name": "John"}
```

So in summary, implementing custom memory requires:

- Storing context in `save_context` 
- Returning memory variables in `load_memory_variables`
- Aligning variable names between memory and chain

## Multiple Memories

As noted in the feedback, more details should be provided on using multiple memory objects.

LangChain makes it straightforward to use multiple memory objects in a single chain. For example:

```python
short_term_memory = ConversationBufferMemory(size=5)
long_term_memory = MyDatabaseMemory() 

chain = MyChain(
   memories=[short_term_memory, long_term_memory]
)
```

The chain will call `load_memory_variables` and `save_context` on each memory. 

To combine variables, memories can be chained:

```python 
class ChainedMemory:

  def __init__(self, memories):
     self.memories = memories

  def load_memory_variables(self, inputs):
     variables = {}
     for memory in self.memories:
       variables.update(memory.load_memory_variables(inputs))  
     return variables
```

So chaining enables merging outputs from multiple memory sources into a single coherent memory context for the chain.

## Persistence

As called out in the feedback, the improved page should cover persistence options.

For memory to span sessions, it must be persisted to disk. LangChain provides integrations for SQL databases.

For example, to use SQLite:

```python
from langchain.memory import SQLiteMemory

memory = SQLiteMemory(url="sqlite:///my_db.sqlite") 
```

Using database storage has implications:

- Makes the system stateful across runs
- Adds I/O overhead for each call
- Requires handling concurrency

So there is a tradeoff between simplicity of in-memory and persistence of databases. LangChain aims to make both easy to use.

## Conclusion

Memory is a vital component for sophisticated conversational AI. LangChain provides utilities for incorporating memory into models, from simple buffers to complex persistent storage. The tools enable starting simple and building custom systems tailored to your conversational needs. Please refer to the documentation for more advanced memory topics.

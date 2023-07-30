

# Improved LangChain Documentation

## Introduction

LangChain is a Python framework for building applications powered by large language models (LLMs). It provides components and tools for:

- **Interfacing with LLMs** - Easily load models like GPT-3 and InstructGPT using the [Model I/O](/docs/modules/model_io) module.

- **Connecting data sources** - Integrate external datasets into your application using the [Data Connection](/docs/modules/data_connection) module. 

- **Constructing workflows** - Chain together sequences of LLM calls, data lookups, and logic using the [Chains](/docs/modules/chains) module. The Chains module allows you to construct prompts, pass user input to LLMs, and sequence calls.

- **Letting chains choose tools** - Create goal-driven chains that dynamically choose tools using the [Agents](/docs/modules/agents) module. The Agents module allows chains to interact with their environment and accomplish high-level tasks.

- **Persisting state** - Maintain conversation context across interactions using the [Memory](/docs/modules/memory) module.

- **Monitoring execution** - Log and analyze chain execution with [Callbacks](/docs/modules/callbacks).

With these modular components, LangChain makes it easy to build complex, data-driven LLM applications like chatbots, semantic search engines, and more.

## Getting Started

To start using LangChain:

1. Install the Python package:

```
pip install langchain
```

2. Follow the [Quickstart Guide](/docs/get_started/quickstart.html) to build your first LangChain app.

3. Check out [example use cases](/docs/use_cases) like chatbots, question answering, and data analysis.

4. Join the [Discord](https://discord.gg/6adMQxSpJS) to connect with other LangChain users.

## Key Modules

LangChain provides the following modules:

### [Model I/O](/docs/modules/model_io)

Interface with language models like GPT-3, BLOOM, and InstructGPT. The Model I/O module allows you to load LLMs and call them with methods like `predict` and `predict_messages`.

```python
from langchain import OpenAI

llm = OpenAI() 
llm.predict("Hello world!")
```

### [Data Connection](/docs/modules/data_connection)

Connect to data sources like SQL, Elasticsearch, and CSVs.

```python
from langchain.data import SQLDatabase

db = SQLDatabase(url="sqlite:///my_database.db")
```

### [Chains](/docs/modules/chains)

Compose sequences of LLM prompts, data lookups, and logic. The Chains module allows constructing sequences of calls to LLMs, databases, and other components.

```python
from langchain import LLMChain, SQLDatabase

db = SQLDatabase(...)  
chain = LLMChain(llm=..., prompt=..., database=db)
```

### [Agents](/docs/modules/agents)

Create goal-driven chains that dynamically choose tools based on high-level directives. The Agents module allows chains to interact with their environment.

```python  
from langchain import Tool, Agent

agent = Agent(tools=[Tool(name="summarize", chain=...),  
                     Tool(name="search", chain=...)])
```

### [Memory](/docs/modules/memory) 

Persist state across chain runs like conversation context.

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory() 
```

### [Callbacks](/docs/modules/callbacks)

Log, monitor, and analyze chain execution.

```python
from langchain import CallbackManager

callbacks = CallbackManager(...)
```

## Resources

- [API Reference](https://api.python.langchain.com)
- [GitHub Repo](https://github.com/hwchase17/langchain)
- [Discord](https://discord.gg/6adMQxSpJS)
- [YouTube Tutorials](/docs/additional_resources/youtube.html)
- [Example Projects](https://github.com/kyrolabs/awesome-langchain)


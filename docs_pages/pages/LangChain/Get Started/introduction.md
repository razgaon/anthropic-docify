 Here is the improved markdown page for the LangChain documentation:

# LangChain Documentation

## Introduction

**LangChain** is a framework for developing applications powered by language models. It enables building applications that are:

* **Data-aware**: Connect language models to external data sources 
* **Agentic**: Allow language models to interact with their environment

The main benefits of LangChain are:

1. **Components**: Abstractions for working with language models, and implementations for each abstraction. Components are modular and easy to use.
2. **Off-the-shelf chains**: Assemblies of components for accomplishing specific tasks 

Off-the-shelf chains make it easy to get started. Components make it easy to customize chains or build new ones.

## Getting Started

Follow these steps to start building with LangChain:

1. [Install](/docs/get_started/installation.html) LangChain 
2. Set up your environment
3. Build your first app by following the [Quickstart](/docs/get_started/quickstart.html) guide 

***Note**: These docs are for the Python package. For [LangChain.js](https://github.com/hwchase17/langchainjs), see [here](https://js.langchain.com/docs).*

## Modules

LangChain provides interfaces and integrations for:

### [Model I/O](/docs/modules/model_io/)

Interface with language models.

**Example:**
```python
from langchain.llms import OpenAI

llm = OpenAI() 
response = llm("Hello!")
```

### [Data Connection](/docs/modules/data_connection/)

Interface with external data sources.

**Example:**
```python
from langchain.data import SQLDatabase

db = SQLDatabase(url="sqlite:///my_data.db")
results = db.query("SELECT * FROM table") 
```

### [Chains](/docs/modules/chains/)

Construct sequences of component calls.

**Example:**
```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
output = chain(input)
```

### [Agents](/docs/modules/agents/) 

Let chains choose tools based on directives.

**Example:**
```python
from langchain.agents import ToolSelectorAgent

agent = ToolSelectorAgent()
tool_chain = agent(task="summarize text") 
```

### Memory

Persist state between chain runs.

**Example:**
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.add_message("Hello")
memory.add_message("Hi there!") 
```

### Callbacks

Log and stream chain steps.

**Example:**
```python 
from langchain.callbacks import ConsoleCallback

callback = ConsoleCallback()
chain.callbacks = callback
chain() # Logs each step
```

## Resources

### [Use Cases](/docs/use_cases/)

Walkthroughs for common applications:

- [Chatbots](/docs/use_cases/chatbots/)  
- [Question answering](/docs/use_cases/question_answering/)
- [Analyzing tabular data](/docs/use_cases/tabular.html)

### [Guides](/docs/guides/)

Best practices for development.

### [Integrations](/docs/integrations/)

Tools that extend LangChain.

### [Ecosystem](/docs/ecosystem/)

Repos that build on LangChain. 

### [YouTube Tutorials](/docs/additional_resources/youtube.html) 

Video tutorials from the community.

### [Gallery](https://github.com/kyrolabs/awesome-langchain)

Curated examples and projects.

## Get Support

Join us on [GitHub](https://github.com/hwchase17/langchain) or [Discord](https://discord.gg/6adMQxSpJS) to connect with the community.

## API Reference

See the [reference docs](https://api.python.langchain.com) for the Python package.
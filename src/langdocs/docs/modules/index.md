

# LangChain Documentation 

## Table of Contents
- [Introduction](#introduction)
- [Modules](#modules)
  - [Model I/O](#model-io)
  - [Data Connection](#data-connection)
  - [Chains](#chains)
  - [Agents](#agents)
  - [Memory](#memory)
  - [Callbacks](#callbacks)
  - [Evaluation](#evaluation)
- [Examples, Ecosystem, and Resources](#examples-ecosystem-and-resources)

## Introduction

**LangChain** is a framework for developing applications powered by **a** language model. It enables applications that are:

* **Data-aware**: Connect a language model to other sources of data
* **Agentic**: Allow a language model to interact with its environment

The main value props of LangChain are:

1. **Components**: Abstractions for working with language models, along with a collection of implementations for each abstraction. Components are modular and easy-to-use, whether you are using the rest of the LangChain framework or not.
2. **Off-the-shelf chains**: A structured assembly of components for accomplishing specific higher-level tasks. 

Off-the-shelf chains make it easy to get started. For more complex applications and nuanced use-cases, components make it easy to customize existing chains or build new ones.

## Modules

LangChain provides standard, extendable interfaces and external integrations for the following modules:

### Model I/O

The Model I/O module provides interfaces for prompting language models and parsing their outputs. It contains the following components:

- **Prompts**: Templatize, dynamically select, and manage model inputs.
- **Language models**: Make calls to language models through common interfaces. For example, the LLM interface allows wrapping text completion models like GPT-3, while the Chat interface allows wrapping conversational models like GPT-4.
- **Output parsers**: Extract information from model outputs.

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=["context", "question"], 
    template="Answer the question based on the context: {context}\n\nQuestion: {question}\nAnswer:"
)

output = llm.predict(
    prompt=prompt.format(
        context="Paris is the capital of France", 
        question="What is the capital of France?"
    )
)

print(output)
# "Paris"
```

### Data Connection

The Data Connection module provides interfaces for connecting language models to external data sources like databases, APIs, etc.

### Chains 

The Chains module provides abstractions for constructing sequences of calls between components. For example, chaining together an LLM call, data fetch, and output parsing.

### Agents

The Agents module builds on top of chains and allows configuring chains that can dynamically decide which tools to use based on high-level directives.

### Memory

The Memory module provides interfaces for persisting state across multiple runs of a chain.

### Callbacks

The Callbacks module provides interfaces for logging and streaming intermediate steps of a chain execution.

### Evaluation

The Evaluation module provides tools for evaluating the performance of chains and components.

## Examples, Ecosystem, and Resources

For examples, integrations, community resources, and more, see the [full documentation](https://langchain.readthedocs.io).


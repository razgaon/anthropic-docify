

# LangChain Documentation

## Overview

LangChain is a Python library for building applications with large language models like GPT-3 and Claude. This documentation provides guides and references to help you develop LangChain applications.

## Getting Started

### Installation

Install LangChain via pip:

```bash
pip install langchain
```

LangChain requires Python 3.7+. 

### Hello World

Here is a simple script to load a model and make a prediction:

```python
from langchain import LLMChain, PromptTemplate

prompt = PromptTemplate(input="Hello world!")

chain = LLMChain(llm="text-davinci-003", prompt=prompt)

print(chain.run())
```

This loads the GPT-3 Davinci text completion model, passes it the prompt "Hello world!", and prints the model's response.

For a more in-depth example, see the [Basic Usage](/docs/use_cases/basic_usage) guide.

## Core Concepts

The core concepts in LangChain are:

### Prompts

Prompts are the inputs passed to models. The [Prompt](/docs/modules/model_io/prompts) module provides ways to parametrize and structure prompts.

For example:

```python
from langchain import PromptTemplate

prompt = PromptTemplate(
    input="Summarize this text:",
    output="Here is a summary:"  
)

print(prompt.format(text="Two roads diverged in a yellow wood..."))
```

This uses a `PromptTemplate` to format the input text into a prompt that asks the model to summarize it. See the [PromptTemplates](/docs/modules/model_io/prompts/prompt_templates) page for more details.

### Models

The [Models](/docs/modules/model_io/models) module provides interfaces to connect with LLMs like GPT-3 and Claude.

For example:

```python
from langchain import OpenAI

llm = OpenAI(model_name="text-davinci-003")

response = llm.predict(prompt="Hello world!")
```

This loads the GPT-3 Davinci model and calls `.predict()` to generate a response. See the [LLMs](/docs/modules/model_io/models/llms) page for more details.

### Output Parsers

[Output parsers](/docs/modules/model_io/output_parsers) extract structured information from model responses.

For example:

```python
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(input="Hello {name}!")
llm = OpenAI(model_name="text-davinci-003")

chain = LLMChain(llm=llm, prompt=prompt, output_parser=HumanNameParser())

response = chain.run(name="Alice")
print(response.parsed) # "Alice"
```

This parses the name from the model's response. See [OutputParsers](/docs/modules/model_io/output_parsers) for more.

## Documentation

- [Modules](/docs/modules)
    - [Model I/O](/docs/modules/model_io)
        - [Prompts](/docs/modules/model_io/prompts)
        - [Models](/docs/modules/model_io/models)
        - [Output Parsers](/docs/modules/model_io/output_parsers)
    - Other modules: Chains, Data, Memory, etc
- [Use Cases](/docs/use_cases) - End-to-end examples and guides
- [API Reference](/docs/api) - Technical reference for all functions and classes




# Installation

## Official Release

To install LangChain, you can use pip or conda:

```
pip install langchain
```

```
conda install langchain -c conda-forge
```

This will install the bare minimum requirements for LangChain. However, to take full advantage of LangChain's capabilities, you will likely need to integrate it with various model providers, data stores, APIs, etc.

There are a couple ways to install LangChain with extra dependencies:

```
pip install langchain[llms]  
# Installs dependencies for common LLM providers like OpenAI, Anthropic, etc.
```

```
pip install langchain[all] 
# Installs dependencies for all integrations.
```

Note: When using zsh, quote square brackets like this: 

```
pip install 'langchain[all]'
```

## From Source

To install from source, clone the repo and run:

```
pip install -e .
```

## Environment Setup

For example, to use LangChain with OpenAI's model APIs:

1. Install the OpenAI Python package:

```
pip install openai
```

2. Get an API key from your OpenAI account and set it as an environment variable:

```
export OPENAI_API_KEY="..."
```

Or pass the key directly when initializing the OpenAI LLM class:

```python
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="...") 
```

See the [Installation Guide](/docs/get_started/installation.html) for more details on environment setup for different providers.


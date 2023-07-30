# Installation

## Overview

LangChain can be installed via **pip** or **conda**. For most use cases, **pip is recommended** as it will provide wider compatibility and more frequent updates. However, if you need to manage many other Python packages and environments, conda may be preferred. 

The bare minimum installation via either method will include just the core LangChain library. For additional functionality, there are two extended installation options:

- `langchain[llms]` - Installs dependencies for common LLM providers like **OpenAI, Anthropic, Cohere** etc. This allows integrating LangChain with popular LLMs out of the box.
- `langchain[all]` - Installs dependencies for **all integrations** LangChain supports, including LLM providers, datastores, APIs, etc. Useful if you want to leverage LangChain's full capabilities, but will install many unneeded packages if you only use a subset of features.

## Installation

### Pip

To install the minimum requirements:

```
pip install langchain
```

To install with LLM provider dependencies:

```
pip install langchain[llms] 
```

To install all integrations:

```
pip install 'langchain[all]'  
```

Note: If using **zsh**, you'll need to quote the brackets to avoid issues.

### Conda

To install with conda:

```
conda install langchain -c conda-forge
```

The conda installation does not support installing optional dependencies like `llms` or `all`. Those would need to be installed separately after the fact.

## Install from Source

To install LangChain from source, clone the GitHub repo and run:

```
pip install -e .
```

This will install LangChain directly from the latest source code. Useful if you want to contribute to LangChain or need the very latest updates before they are released.

## Next Steps

With LangChain installed, you can now [setup your environment](/docs/get_started/setup) and start [building applications](/docs/get_started/building_applications)!

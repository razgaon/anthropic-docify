
# Installation

There are a few different ways to install LangChain depending on your needs:

## Using pip

You can install LangChain via pip by running:

```
pip install langchain
```

This will install the core LangChain library with the minimum requirements needed to get started.

To install modules for integrating with common LLM providers:

```
pip install 'langchain[llms]'
```

To install modules for all integrations like databases and search: 

```
pip install 'langchain[all]'  
```

## Using conda

If you use the conda package manager, you can install LangChain by running:

```
conda install langchain -c conda-forge
```

This will install the core library. To install extras:

```
conda install 'langchain[llms]' -c conda-forge
```

```
conda install 'langchain[all]' -c conda-forge
```

## Verifying Installation

After installation, you can verify it worked correctly by running:

```python
import langchain
print(langchain.__version__)
```

## Installing from source

To install the latest version from source:

1. Ensure you have git installed 
2. Clone the repository:

```
git clone https://github.com/hwchase17/langchain.git
```

3. Install with pip in editable mode:

```
pip install -e .
```

This will let you edit the source code directly and have the changes be reflected. See the [contributing guide](https://github.com/hwchase17/langchain/blob/main/CONTRIBUTING.md) for more details on setting up a development environment.




# Toolkits

Toolkits are collections of tools designed to be used together for specific tasks. They provide convenience loading methods to initialize the tools with a single function call.

For example, you can load a QA toolkit that bundles together a question answering agent, a search tool, and a summarization tool to enable complex workflows with just:

```python
from langchain.toolkits import load_qa_toolkit

qa_tools = load_qa_toolkit(llm)
```

This handles initializing each tool with the provided llm and returning them ready to use.

# Tools 

Tools provide interfaces that agents can use to interact with the world. Tools can be things like:

- Chains  
- Other agents
- Search utilities
- Summarization models
- Translation models

Some tools like chains and agents require a base LLM to initialize. You can pass in an LLM when loading tools:

```python  
from langchain.agents import load_tools

tool_names = [...]
llm = ...
tools = load_tools(tool_names, llm=llm)
```

This will initialize the tools that need an LLM with the provided one.

# Document Loaders

Document loaders are used to load data from different sources as `Document` objects. A `Document` combines text content with associated metadata. 

For example, there are document loaders for:

- Loading text files
- Scraping the text contents of a web page  
- Loading transcripts of YouTube videos

Document loaders expose a `load` method to load data from a source as `Document` objects. Many also implement `lazy_load` to lazily load data into memory only when needed.

Here is an example loading a Markdown file:

```python
from langchain.document_loaders import TextLoader

loader = TextLoader("./index.md")  
docs = loader.load()
```

This loads the Markdown file as a single `Document` object.


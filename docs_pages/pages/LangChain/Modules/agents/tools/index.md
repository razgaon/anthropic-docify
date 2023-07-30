 # Tools

## Introduction

Tools are interfaces that agents can use to interact with the world. LangChain provides a flexible framework for loading and using tools to build agentic systems. 

This guide covers:

- Loading tools
- Tool design
- Caching and lazy loading
- Tool examples

## Loading Tools

Tools are functions that agents can call to take actions and gather information. Tools can be generic utilities, chains, or even other agents. 

To load tools, use the `load_tools` function:

```python
from langchain.agents import load_tools

tool_names = ["search", "summarize"] 
tools = load_tools(tool_names)
```

Some tools like chains and agents need a language model (LLM) to initialize. Pass in an LLM: 

```python
from langchain.agents import load_tools

tool_names = ["search", "summarize"]
llm = MyLLM()
tools = load_tools(tool_names, llm=llm)
```

## Tool Design

Effective tools should have the following qualities:

- **Well-defined interfaces** - Tools should expose a clear interface for agents to call, with predictable input and output schemas. Avoid complex nested logic.

- **Loose coupling** - Tools should not depend heavily on each other or share state. This makes them modular and reusable.

- **Single responsibility** - Each tool should focus on one capability to keep the logic simple.

- **Pure functions** - Tools should return the same output for the same input and avoid side effects where possible.

- **Lazy loading** - Tools should lazy load any expensive initialization logic until they are called to optimize performance.

## Caching and Lazy Loading

Tools are cached and lazily loaded in LangChain. This means:

- Tools are only initialized when first called, not when loaded. This optimizes performance.

- Once initialized, tools are cached and reused. Loading the same tool multiple times will reuse the cached instance.

So feel free to load tools wherever needed. The caching and lazy loading will ensure optimal performance.

## Tool Examples

Here are some examples of using tools:

**Search**

```python
search_tool = tools["search"] 

results = search_tool("langchain", num_results=5)
```

**Summarize** 

```python
summary_tool = tools["summarize"]

text = load_text("article.txt")
summary = summary_tool(text, max_length=100)
```

**Browser**

```python 
from langchain.tools import BrowserTool

browser = BrowserTool()

browser.goto("https://blog.langchain.dev")
page_text = browser.extract_text()
```

**SQL**

```python
from langchain.tools import SQLTool

sql = SQLTool(database_url) 

results = sql("SELECT * FROM users WHERE age > 30")
```

## Conclusion

This covers the key concepts for working with tools in LangChain. The flexible loading and caching makes it easy to assemble tools into powerful agentic systems. With the guidelines on tool design, you can create modular, reusable tools. Refer to the examples and [integrations](/docs/integrations/tools) for more on building with specific tool types.
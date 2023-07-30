

Tools
=====

Tools are interfaces that allow agents to interact with the world. Tools can be generic utilities, chains, or even other agents. This guide covers key concepts for working with tools in LangChain.

## Defining Custom Tools

Custom tools are Python functions decorated with the `@tool` decorator. This handles converting the function into a format invokable by the agent.

Tools take input parameters and return outputs. Type annotations can be used to specify input and output types:

```python
from langchain.agents import tool

@tool
def my_tool(text: str) -> str:
  return text.upper()
```

The tool above takes a string as input and returns the uppercase version of the string.

## Loading Tools

To load tools and make them available to an agent, use the `load_tools` function:

```python
from langchain.agents import load_tools

tool_names = ["my_tool"]
tools = load_tools(tool_names) 
```

This loads the tools based on the name.

Some tools require initializing with a base LLM. You can pass the LLM: 

```python
llm = ... # LLM instance 

tools = load_tools(tool_names, llm=llm)
```

This initializes the tools using the provided LLM.

## Using Tools

The loaded tools can be passed to the agent and executor:

```python
agent = MyAgent(tools=tools)
executor = AgentExecutor(agent=agent, tools=tools) 
```

This allows the agent access to the tools through the executor.

In summary, tools allow agents to take actions. Defining, loading, and passing tools to an agent enables rich functionality.

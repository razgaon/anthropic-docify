

# Building a ReAct Agent

## Overview

This guide covers using LangChain to build a ReAct agent, including customizing the agent and tools, adding memory for conversation, debugging tips, and more. ReAct agents follow an observe-think-act cycle to decompose tasks and use tools to gather information.

## Getting Started 

To create a basic ReAct agent:

```python
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0)

@tool  
def get_word_length(word: str) -> int:
  """Returns the length of a word."""
  return len(word)
  
tools = [get_word_length]

from langchain.schema import SystemMessage
system_message = SystemMessage(content="You are very powerful assistant, but bad at calculating lengths of words.")
prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_message)

from langchain.agents import OpenAIFunctionsAgent
agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)

from langchain.agents import AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.run("how many letters in the word educa?")
```

This loads a chat model, defines a custom tool to get word lengths, creates a prompt, initializes an agent, and runs it to get the length of a word.

## Customizing the Agent

The agent can be customized by:

- Changing the base agent class used (ReAct, OpenAI Functions, etc)
- Defining custom tools as Python functions 
- Modifying the prompt with different instructions, context, etc

For example:

```python
@tool
def get_actor_info(name: str) -> str:
  # Lookup actor bio 
  return lookup_actor_bio(name)

prompt = """You are an AI assistant focused on movies...""" 

tools = [get_word_length, get_actor_info]
```

## Adding Memory

To make the agent conversational, memory can be added:

```python 
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history")

# Add memory to the executor, not the agent
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True) 
```

The prompt also needs to be updated to store conversation context.

## Debugging Tips

- Use `verbose=True` to see the full agent thought process  
- Test tools in isolation to validate they work as expected
- Log and inspect observations after each tool call
- Modify prompt to print more reasoning steps

## Summary

- ReAct agents are highly customizable for different use cases
- Tools and prompts can be modified to change capabilities
- Memory enables conversational agents 
- Enable verbose logging and test tools when debugging


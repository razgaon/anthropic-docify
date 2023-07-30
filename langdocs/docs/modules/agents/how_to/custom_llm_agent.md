# Custom LLM Agents

This guide covers how to build custom LLM agents using LangChain. We'll walk through setting up the environment, tools, prompt template, output parser, LLM, stop sequence, and agent executor.

## Overview

An LLM agent consists of four key components:

- **Prompt Template**: Provides instructions for the LLM on what to do. This allows controlling the agent's behavior.
- **LLM**: The large language model that powers the agent. Different models have different capabilities.
- **Stop Sequence**: A special token that tells the LLM when to stop generating text. This is critical to prevent runaway generation.
- **Output Parser**: Parses the raw LLM text into structured `AgentAction` or `AgentFinish` objects. This handles the interface between the LLM and the outside world.

The agent is used in an **Agent Executor** loop:

1. User input is passed to the agent
2. The agent returns either an `AgentAction` or `AgentFinish`
3. If it is an `AgentAction`, the executor calls the specified tool and gets an `Observation`
4. The executor repeats the loop, passing the `AgentAction` and `Observation` back to the agent until an `AgentFinish` is returned

This loop allows the agent to take multiple actions before returning a final response.

## Set up Environment

Import the necessary libraries:

```python
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, SerpAPIWrapper, LLMChain
from typing import List, Union
from langchain.schema import AgentAction, AgentFinish, OutputParserException
import re
```

## Set up Tools

Define any tools the agent can use:

```python
# Search tool
search = SerpAPIWrapper()

tools = [
  Tool(
    name="Search",
    func=search.run,
    description="Useful for answering questions about current events"
  )
]
```

## Prompt Template

Instruct the agent on what to do:

```python
# Template
template = """
You are a helpful assistant with access to these tools:

{tools}

Please follow this format:

Question: {input}
Thought: Think about how to answer the question
Action: Tool to use
Action Input: Input for the tool
Observation: Result from tool
Final Answer: Final response to the original question

{agent_scratchpad}
"""

# Prompt class
class CustomPrompt(StringPromptTemplate):

  def format(self, **kwargs):

    thoughts = ""

    for action, obs in kwargs["intermediate_steps"]:
      thoughts += f"{action.log}\nObservation: {obs}\n"

    kwargs["agent_scratchpad"] = thoughts

    kwargs["tools"] = "\n".join([
      f"{t.name}: {t.description}" for t in self.tools
    ])

    return self.template.format(**kwargs)

prompt = CustomPrompt(
  template=template,
  tools=tools,
  input_variables=["input", "intermediate_steps"]
)
```

The template provides instructions and formats the tools, previous steps, and input.

## Output Parser

Parse LLM output into `AgentAction` or `AgentFinish`:

```python
class CustomOutputParser(AgentOutputParser):

  def parse(self, llm_output: str):

    if "Final Answer:" in llm_output:
      return AgentFinish(
        return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
        log=llm_output
      )

    match = re.search(r"Action: (.*)\nInput: (.*)", llm_output, re.DOTALL)

    if not match:
      raise OutputParserException("Could not parse output")

    action = match.group(1).strip()
    action_input = match.group(2).strip()

    return AgentAction(
      tool=action,
      tool_input=action_input,
      log=llm_output
    )

parser = CustomOutputParser()
```

This parses the raw LLM output into structured objects.

## Set up LLM

Choose your LLM:

```python
llm = OpenAI(temperature=0)
```

## Stop Sequence

Tell the LLM when to stop generating:

```python
stop = ["\nObservation:"]
```

This aligns with the `Observation` token in the prompt.

## Create Agent

Combine the components:

```python
llm_chain = LLMChain(llm=llm, prompt=prompt)

agent = LLMSingleActionAgent(
  llm_chain=llm_chain,
  output_parser=parser,
  stop=stop,
  allowed_tools=[t.name for t in tools]
)
```

## Use the Agent

Run the executor:

```python
executor = AgentExecutor.from_agent_and_tools(
  agent=agent,
  tools=tools,
  verbose=True
)

executor.run("How many people live in Canada?")
```

## Debugging Tips

Some tips for debugging agents:

- Log intermediate LLM outputs to see full responses
- Print parsed `AgentAction` and `AgentFinish` objects
- Ensure stop sequence aligns with prompt format
- Test output parser on sample LLM outputs
- Simplify prompt and output parsing format if needed
- Adjust LLM temperature if getting inconsistent outputs

Careful prompt design, output parsing, and debugging allows building effective custom agents!

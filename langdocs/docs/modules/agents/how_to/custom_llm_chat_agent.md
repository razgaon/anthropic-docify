

Here is my attempt at rewriting the reference page with the improvements:

# Building a Custom LLM Agent

This guide covers how to build your own custom LLM agent using LangChain. We'll go over the key components needed, provide examples and code snippets, and share tips on troubleshooting and debugging.

## Overview

The main pieces needed to build a custom LLM agent are:

- **Prompt Template**: Instructions for the LLM on what to do  
- **LLM**: The language model that powers the agent
- **Output Parser**: Parses LLM output into actions
- **Tools**: External functions the agent can call
- **Agent**: Combines the above components  
- **AgentExecutor**: Runs the agent loop

We'll cover each section in detail below.

## Prompt Template

The prompt template tells the LLM how to format its output and what actions it can take.

```python
# Example prompt template 

class MyPrompt(BasePromptTemplate):

  def format(self, input, tools):
    
    return f"""

Answer the question: {input} 

You have access to the following tools:

{tools}

Use this format:

Action: {action}  
Input: {input}
Output: {output}

Final Answer: 
"""
```

The template should include placeholders for:

- User input  
- Available tools
- Action, input, output for tool invocations
- Final answer

## Output Parser

The output parser takes the raw LLM output and converts it into `AgentAction` and `AgentFinish` objects.

```python
# Example output parser

class MyOutputParser(AgentOutputParser):

  def parse(self, output):
    
    if "Final Answer" in output:
      return AgentFinish(output)
    
    action, input = parse_action(output)
    return AgentAction(action, input) 
```

- Use regex or string matching to parse actions
- Raise exceptions on failures to debug

## LLM

Any LLM can be used including OpenAI, Anthropic, Cohere etc.

```python
llm = OpenAI() 
# or
llm = Anthropic()
``` 

Adjust temperature, top-p, etc to improve performance.

## Tools

Tools are external functions the agent can invoke:

```python 
@tool
def search(input):
  # Call search API
  return results

tools = [search] 
```

Expose tools to the agent via the prompt template.

## Agent

Bring the components together into an agent:

```python
agent = LLMAgent(
  llm=llm,
  prompt=prompt,
  output_parser=parser, 
  tools=tools
)
```

## AgentExecutor 

The executor runs the agent loop:

```python 
executor = AgentExecutor(agent=agent)
executor.run(user_input) 
```

Pass tools again to executor to call them.

## Troubleshooting

- **Prompt issues**: Start with a simple prompt and incrementally add complexity. Verify each component (tools, actions, etc) works before moving on.

- **Output parser failures**: Log and inspect raw LLM output on failures. Check for mismatches between prompt and parser. For example, if the parser expects "Final Answer" but the prompt does not include it.

- **Incorrect behaviors**: Increase temperature for more diversity. Use penalties to adjust behaviors. For example, if the agent is too verbose or repetitive.

- **Logging**: Log LLM requests/responses, tool invocations, parsed actions etc for debugging. This can help narrow down where issues are occurring.


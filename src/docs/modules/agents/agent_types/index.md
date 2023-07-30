

# Agent Types

Agents in LangChain leverage large language models to determine the sequence of actions to take to accomplish a goal. The key components of an agent are:

- **Agent**: Responsible for deciding the next action using a prompt and LLM.
- **Tools**: Functions the agent can call as actions. Proper tool design and description is critical.  
- **Toolkits**: Groups of tools needed for common objectives.
- **AgentExecutor**: The runtime that executes the agent loop.

LangChain provides several pre-built agent types:

## Zero-shot ReAct

This agent uses the [ReAct](https://arxiv.org/pdf/2205.00445.pdf) framework to choose tools based on their descriptions. Tools must have descriptions.

**Note**: Most general purpose action agent.

## Structured Input ReAct

Uses ReAct framework but can handle tools with complex multi-input APIs instead of just string inputs. Useful for things like browser automation.

## OpenAI Functions 

Uses models like GPT-3.5 fine-tuned to detect functions calls. Requires ChatGPT-style models.

## Conversational

Designed for conversation. Uses ReAct and memory to have dialogs.

## Self Ask with Search

Implements [self-ask](https://ofir.io/self-ask.pdf) by using a single `Intermediate Answer` tool to lookup facts.

## ReAct Document Store

Uses ReAct to search documents and lookup info with `Search` and `Lookup` tools. Matches the Wikipedia agent in the [ReAct paper](https://arxiv.org/pdf/2210.03629.pdf).

## Plan and Execute

Plans high-level tasks by breaking them down into subtasks, then executes those subtasks. Inspired by [BabyAGI](https://github.com/yoheinakajima/babyagi) which uses hierarchical planning. Also related to ["Plan-and-Solve"](https://arxiv.org/abs/2305.04091) which interleaves planning and execution. The agent plans using the LLM, then executes tools for subtasks. Useful for accomplishing long-term objectives that require multiple steps.

```python
from langchain.agents import PlanAndExecuteAgent

agent = PlanAndExecuteAgent(llm, tools, plan="Make me a sandwich") 

agent_executor = AgentExecutor(agent, tools)
agent_executor.run() # Agent plans then executes subtasks
```

## Comparison

| Agent Type | Conversational | Required Tools | Flexibility | Use Cases |
|-|-|-|-|-|  
| Zero-shot ReAct | No | Tool descriptions | High | General problem solving |
| Structured Input ReAct | No | Tool descriptions and schemas | Medium | Browser automation, APIs |
| OpenAI Functions | Yes | None | Low | Conversation |
| Conversational | Yes | Tool descriptions | Medium | Conversation |
| Self Ask with Search | No | Fact lookup tool | Low | Question answering |
| ReAct Document Store | No | Search and lookup tools | Medium | Searching documents |
| Plan and Execute | No | Task-specific | Low | Long-term planning |

# Get Started Building an Agent

Here is an annotated code example of building a custom agent with personality, tools, and memory:

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

# Load chat model
llm = ChatOpenAI(temperature=0)

# Define tools  
@tool
def get_word_length(word: str) -> int:
  """Returns length of a word"""
  return len(word)

# Set system message
system_message = SystemMessage(
  content="You are very powerful but bad at word lengths"
)

# Add memory placeholder 
MEMORY_KEY = "chat_history"
prompt = OpenAIFunctionsAgent.create_prompt(
  system_message=system_message,
  extra_prompt_messages=[MessagesPlaceholder(variable_name=MEMORY_KEY)] 
)

# Initialize memory
memory = ConversationBufferMemory(memory_key=MEMORY_KEY, return_messages=True)

# Initialize agent
agent = OpenAIFunctionsAgent(
  llm=llm,
  tools=[get_word_length],
  prompt=prompt
)

# Run agent with memory
agent_executor = AgentExecutor(
  agent=agent, 
  tools=[get_word_length],
  memory=memory,
  verbose=True
)

agent_executor.run("How many letters in educa?")  
agent_executor.run("Is that a real word?") # Uses memory
```

This shows adding memory to enable conversations. See the [agent documentation](https://docs.langchain.dev/modules/agents) for more examples.

# Tools 

Tools are functions the agent can call as actions. Some key design considerations:

- **Granularity**: Tools should encapsulate a useful but focused capability. Avoid large, complex tools.

- **Interfaces**: Tools can take simple string inputs or complex structured inputs with typing and schemas.

- **Idempotence**: Tools should provide the same output given the same input to avoid confusing the agent.

- **Descriptions**: Write clear descriptions explaining what the tool does in plain language.

See the [tools documentation](https://docs.langchain.dev/modules/agents/tools) for more on designing effective tools.

# Training Agents

Here are some best practices for training agents:

- **Prompt Engineering**: Carefully design the prompt to provide the right context, personality, and prompting strategies. Test different phrasings.

- **Self-Play**: Have the agent practice conversations with itself to learn.

- **Human-in-the-Loop**: Have humans chat with the agent and provide feedback to improve.

- **Retraining**: Periodically retrain the agent on new conversations to keep improving.

- **Model Selection**: Try different LLMs to find the best fit. Models with more capabilities like GPT-3.5 often perform better.

The key is continuously training the agent through conversation and feedback. Agents learn best by doing, not just passively reading.


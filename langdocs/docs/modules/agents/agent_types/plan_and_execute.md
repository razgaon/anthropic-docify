

# Plan and Execute Agents

## Introduction

Plan and execute agents accomplish objectives by first planning what to do, then executing the subtasks. This approach is inspired by [BabyAGI](https://github.com/yoheinakajima/babyagi) and the ["Plan-and-Solve" paper](https://arxiv.org/abs/2305.04091). 

The key components are:

- **Planner**: An LLM that plans the steps to accomplish the objective
- **Executor**: An agent that executes the planned steps using tools
- **Agent**: The overall agent that invokes the planner and executor

## Concepts

### Planner

The planner is responsible for determining the sequence of steps needed to accomplish the objective. As noted in the FAQ, this planning is almost always done by an LLM, usually a conversational model like ChatGPT.

Some examples of planners:

- `load_chat_planner` - Loads a ChatGPT-style model to act as the planner
- Custom planning LM - You can use any LLM as the planner

### Executor 

As stated in the FAQ, the execution is usually done by a separate agent equipped with tools. The executor runs the sequence of steps output by the planner. It does this by invoking tools based on the planner's instructions.

The executor handles complexities like:

- Handling cases where the planner specifies non-existent tools
- Logging and observability of all actions and tool invocations

Some examples of executors:

- `load_agent_executor` - Loads a ChatGPT-style model along with tools
- Custom executor - You can build a custom executor tailored to your tools

### Agent

The agent is the overall class that combines the planner and executor. It invokes the planner to get the plan, then passes the plan to the executor to run it.

Some examples of agents:

- `PlanAndExecute` - Combines a planner LM and executor agent  
- `BabyAGI` - Implementation of the BabyAGI architecture

## Usage

Here is an example of using the `PlanAndExecute` agent:

```python
from langchain.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner

model = ChatOpenAI(temperature=0)

planner = load_chat_planner(model)  
executor = load_agent_executor(model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")
```

This uses `load_chat_planner` and `load_agent_executor` to create the planner and executor, combines them into a `PlanAndExecute` agent, and runs the agent.

The agent will first plan the steps needed, like searching for the girlfriend and calculating the age, before executing them.

## Real-World Examples

Some real-world examples where plan and execute agents could be useful:

- **Customer support** - Plan steps like looking up account details, checking order status, refunding purchases etc.
- **Data gathering** - Plan steps like API calls, web scraping, filtering and processing data  
- **Research assistance** - Plan steps like searching papers, summarizing key points, generating visualizations

By planning complex tasks as sequences of simpler steps, these agents can automate workflows in many domains.


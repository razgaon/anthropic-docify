

# Agents

Agents allow using a language model to dynamically determine the sequence of actions to take to accomplish a task. This is in contrast to chains, where the sequence of actions is hardcoded. 

## Key Components

### Agent

The agent is the class responsible for deciding the next action to take based on the prompt, tools available, and previous actions taken. The prompt provides context like the agent's personality and background. Popular agent types include [ReAct](/docs/modules/agents/agent_types/react.html) and [OpenAI Functions](/docs/modules/agents/agent_types/openai_functions_agent.html).

### Tools 

Tools are functions the agent can call as actions. Key considerations:

- Providing the right tools for the task
- Describing tools in a way the agent understands

LangChain provides many prebuilt tools like [search](/docs/modules/agents/tools/search.html) and [web](/docs/modules/agents/tools/web.html). It's also easy to define custom tools.

### Toolkits

Toolkits are groups of 3-5 related tools the agent needs to accomplish a specific task. For example, the [search toolkit](/docs/modules/agents/toolkits/search.html) contains tools for web search and scraping. LangChain provides many prebuilt toolkits.

### AgentExecutor

The AgentExecutor runs the agent loop:

1. Get action from agent 
2. Execute action (call tool)
3. Send observation to agent
4. Repeat until agent returns `AgentFinish`

It handles errors and logging.

## Getting Started

To build a custom agent:

1. Choose an [agent type](/docs/modules/agents/agent_types/) like ReAct
2. Create a prompt with agent personality/context 
3. Define tools for the task
4. Construct the agent by passing the prompt, tools etc.
5. Run the agent in an AgentExecutor

See the [full example](/docs/use_cases/building_conversational_agents/custom_agent.html).


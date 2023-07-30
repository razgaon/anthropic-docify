

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

The AgentExecutor runs the loop that executes the agent's chosen actions. It:

- Calls the agent to get the next action 
- Executes the action tool 
- Feeds the observation back to the agent
- Continues until the agent returns `AgentFinish`

It also handles errors and logging.

## Getting Started

To build a custom agent:

1. Choose an [agent type](/docs/modules/agents/agent_types/) like ReAct
2. Define relevant [tools](/docs/modules/agents/tools/)
3. Create a prompt with tool info 
4. Instantiate the agent class
5. Run it with an AgentExecutor

See the [custom agent example](/docs/use_cases/autonomous_agents/custom_agent.html) for sample code.

## Additional Resources

- [Agent types](/docs/modules/agents/agent_types/) - Details on different agent algorithms 
- [Tools](/docs/modules/agents/tools/) - Available tools
- [Toolkits](/docs/modules/agents/toolkits/) - Prebuilt tool groups
- [AgentExecutor](/docs/modules/agents/agent_executor.html) - Runtime class
- [Examples](/docs/use_cases/autonomous_agents/) - Code samples for custom agents


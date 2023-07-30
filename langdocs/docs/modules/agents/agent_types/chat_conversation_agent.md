

# Conversational Agents

## Overview

Conversational agents in LangChain are designed to have natural conversations with users, unlike traditional goal-oriented agents. This is accomplished using the `conversational-react-description` agent type along with a memory component.

## Initializing the Conversational Agent

To create a conversational agent, you need to:

1. Define tools like search that the agent can use
2. Initialize a memory component
3. Initialize the agent by passing the tools, LLM, and memory

```python
from langchain.agents import Tool  
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent

search = SerpAPIWrapper()
tools = [
  Tool(
    name = "Current Search",
    func=search.run,
    description="useful for when you need to answer questions about current events or the current state of the world"
  ),
]

memory = ConversationBufferMemory(memory_key="chat_history") 

llm=OpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
```

## Using Memory

The `ConversationBufferMemory` tracks chat history and context.

```python
from langchain.prompts import MessagesPlaceholder

chat_history = MessagesPlaceholder(variable_name="chat_history")

memory = ConversationBufferMemory(
  memory_key="chat_history", 
  return_messages=True,
  prompt=chat_history
)
```

You can customize the memory prompt to control how chat history is formatted.

## Training Conversational Models

Fine-tuning on conversational data can improve coherence.

```python
from langchain.llms import OpenAI
from langchain.chains import ConversationChain

llm = OpenAI(temperature=0)
chain = ConversationChain(llm=llm)

conv_dataset = [
  ("hi", "hello there!"),
  ("what's your name?", "I'm Clara, nice to meet you!"),
  ("how are you today?", "I'm doing great, thanks for asking!") 
]

chain.fine_tune(conv_dataset, batch_size=8, epochs=20)
```

Use a low learning rate like 1e-6 to gently fine-tune the model.

## Troubleshooting

If you see repetitive or inconsistent responses:

- Lower the temperature to increase determinism 
- Adjust the memory prompt formatting
- Fine-tune on more conversational data
- Try different prompt engineering strategies

## Conclusion

With the right setup of tools, memory, and training, conversational agents in LangChain can enable natural dialog. Monitor logs and experiment with customization to improve performance.


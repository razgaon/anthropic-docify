

# Replicating MRKL

## Overview

MRKL (Modular Retrieval-Based Knowledge Learner) is an AI system that combines different modular tools like search engines, databases, and calculators with a foundation language model. It can dynamically select and coordinate these skills to answer diverse questions across domains like math, databases, and general knowledge. 

This guide demonstrates how to replicate MRKL's core capabilities using the LangChain library.

## Prerequisites

Before creating the MRKL agent, we need to set up the environment and install dependencies:

```
pip install langchain
pip install sqlite 
```

We will also need to set up a sample SQLite database. Follow the instructions [here](https://database.guide/2-sample-databases-sqlite/) to download the Chinook database and place the `.db` file in your project. 

## Creating the Agent

We first initialize the tools that MRKL needs:

```python
from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
from langchain.agents import initialize_agent, Tool   
from langchain.agents import AgentType

llm = OpenAI(temperature=0)  
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain(llm=llm, verbose=True) 

db = SQLDatabase.from_uri("sqlite:///chinook.db")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

tools = [
  Tool(
   name = "Search",
   func=search.run,
   description="Useful for current events. Ask targeted questions."
  ),

  Tool(  
   name="Calculator",
   func=llm_math_chain.run,
   description="Useful for math questions."
  ),
   
  Tool(
   name="Music DB", 
   func=db_chain.run,
   description="Useful for music data questions. Input should be a question with context."
  )
]
```

We wrap the database and math tools in standardized LangChain chains. 

The agent can then be initialized:

```python
mrkl = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
```

We pass the tools, LLM, and specify `AgentType.ZERO_SHOT_REACT_DESCRIPTION` for the coordination logic.

The agent could also be customized - for example, using a different `AgentType` or configuring the tools differently.

## Usage Examples

Let's see some examples of using the MRKL agent:

### Girlfriend Age Calculation

```python
mrkl.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")
```

The agent first uses the Search tool to identify the girlfriend as Camila Morrone. It then uses the Calculator tool to perform the math operation on her age.

### Music Database Query

```python 
mrkl.run("What is the full name of the artist who recently released an album called 'The Storm Before the Calm' and are they in the Music DB? If so, what albums of theirs are in the database?")
```

Here the agent uses Search to find the artist name Alanis Morissette. It then queries the Music DB to check if she is present and list her albums.

In both cases, the agent combines its modular tools to answer the multi-part questions.

## Summary

This demonstrates how MRKL can be replicated in Python using the LangChain library. The key ideas are:

- Creating modular tools for different skills 
- Initializing an agent with coordination logic
- Dynamically selecting tools based on the question

With more advanced training, modular architectures like this could enable very capable AI assistants.


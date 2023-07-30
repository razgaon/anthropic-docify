

# OpenAI Functions Agent

The OpenAI Functions API allows you to describe functions that you want an AI model to call. The model will intelligently output arguments to invoke those functions. This allows reliably generating valid function calls compared to generic text generation. 

Certain OpenAI models (like gpt-3.5-turbo-0613 and gpt-4-0613) have been fine-tuned to detect when a function should to be called and respond with the inputs that should be passed to the function. In an API call, you can describe functions and have the model intelligently choose to output a JSON object containing arguments to call those functions. The goal of the OpenAI Function APIs is to more reliably return valid and useful function calls than a generic text completion or chat API.

The OpenAI Functions Agent in LangChain is designed to work with these models.

## Installation

The `openai` and `google-search-results` packages are required:

```
pip install openai google-search-results
```

## Imports

```python
from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
from langchain.agents import initialize_agent, Tool 
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
```

The key classes we will use:

- `ChatOpenAI` - Chat model 
- `Tool` - Represents a function the agent can call
- `initialize_agent` - Creates the agent

## Initializing Tools

We first create the tools available to the agent. Here are a few examples:

```python
# Search tool 
search = SerpAPIWrapper()

# Math tool
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

# Database tool 
db = SQLDatabase.from_uri("sqlite:///path/to/db.sqlite")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

tools = [
  Tool(
   name = "Search",
   func=search.run,
   description="Useful for answering questions about current events. Ask targeted queries."
  ),

  Tool(
    name="Calculator",
    func=llm_math_chain.run,
    description="Useful for answering math questions."
  ),
  
  Tool(
   name="MyDatabase",
   func=db_chain.run,
   description="Useful for querying the MyDatabase database." 
  )
]
```

We initialize various tools like:

- `Search` - A search engine wrapper 
- `Calculator` - A math calculation tool powered by an LLM
- `MyDatabase` - A database query tool

## Initializing the Agent

We can now create the agent by passing the tools and base LLM:

```python
agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)
```

We specify the `AgentType.OPENAI_FUNCTIONS` to enable function invocation.

## Usage

We can now use the agent to invoke the tools:

```python
# Invoke search 
agent.run("Who won the superbowl in 2022?")

# Invoke calculator
agent.run("What is the square root of 144?") 

# Invoke database  
agent.run("What are the top 3 tracks by play count in MyDatabase?")
```

The agent will:

1. Analyze the question
2. Choose the right tools to invoke 
3. Invoke the tools
4. Construct the full response

This allows easily combining multiple skills into a single intelligent agent!

The initialization, tools, and execution can be customized in many ways to suit your needs. Please refer to the documentation for additional examples and options.


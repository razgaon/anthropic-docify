 Here is the improved markdown page for the LangChain structured tool chat documentation:

# Structured Tool Chat

The structured tool chat agent allows developers to use tools with complex, structured inputs in LangChain agents. This enables more advanced integrations between agents and external APIs, databases, browsers, and more. 

## Overview

Older LangChain agents are configured to specify action inputs as simple string prompts. However, many real-world tools require more complex, structured inputs like JSON objects or function arguments.

The `structured-chat-zero-shot-react-description` agent can utilize tools' `args_schema` to generate structured action inputs dynamically. This unlocks more powerful integrations without requiring custom engineering.

## Usage

To use structured action inputs, initialize an agent with the `AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION` type:

```python
from langchain.agents import AgentType
from langchain.agents import initialize_agent

agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION) 
```

Then ensure your tools have an `args_schema` defined that specifies the required input parameters:

```python
from langchain.tools import Tool

tool = Tool(
  name="My Tool",
  func=my_tool_function,
  args_schema=[
    {"name": "param1", "type": "str", "description": "The first parameter"},
    {"name": "param2", "type": "int", "description": "The second parameter"}
  ]
)
```

The agent will use the `args_schema` to construct structured action inputs like:

```json
{
  "action": "My Tool",
  "action_input": {
    "param1": "hello",
    "param2": 42
  }
}
```

## Examples

Let's look at some examples of using structured action inputs:

### Browser Automation

We can integrate with a browser using tools that take structured inputs:

```python
from langchain.tools import Tool
from langchain.agents import initialize_agent
from playwright.async_api import async_playwright

async def goto(page, url):
  await page.goto(url)
  
async def get_text(page, selector):
  element = await page.query_selector(selector)
  return await element.inner_text()

browser = await async_playwright().start() 
page = await browser.new_page()

tools = [
  Tool(name="Goto", func=goto, args_schema=[{"name": "url", "type": "str"}]),
  Tool(name="Get Text", func=get_text, args_schema=[{"name": "selector", "type": "str"}]) 
]

agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)

response = agent.run("Go to example.com and get the page header text")
```

The agent can now use these tools with the proper structured inputs:

```
{
  "action": "Goto",
  "action_input": {"url": "example.com"} 
}

{
  "action": "Get Text", 
  "action_input": {"selector": "h1"}
}
```

### API Integration

Structured inputs enable direct integration with API endpoints:

```python
import requests

def call_api(endpoint, params):
  response = requests.get(f"https://api.example.com/{endpoint}", params=params)
  return response.json()
  
tools = [
  Tool(name="API Call", func=call_api, args_schema=[
    {"name": "endpoint", "type": "str"}, 
    {"name": "params", "type": "dict"}
  ])
]

agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION) 

response = agent.run("Call the users endpoint to get user 123")
```

The agent can construct the structured input:

```
{
  "action": "API Call",
  "action_input": {
    "endpoint": "users",
    "params": {"id": 123}
  }  
}
```

### Database Queries

We can integrate SQL databases using tools that take queries as structured inputs:

```python 
import psycopg2

def query_db(sql):
  conn = psycopg2.connect(DB_URL)
  cur = conn.cursor()
  cur.execute(sql)
  return cur.fetchall()

tools = [
  Tool(name="Query", func=query_db, args_schema=[{"name": "sql", "type": "str"}])  
]

agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)

response = agent.run("Get users aged 20-30 from the database") 
```

The agent can construct a proper SQL query:

```
{
  "action": "Query",
  "action_input": {
    "sql": "SELECT * FROM users WHERE age BETWEEN 20 AND 30"
  }
}
```

## Conclusion

Structured action inputs enable LangChain agents to integrate with real-world APIs, browsers, databases, and more. By leveraging tools' argument schemas, agents can dynamically construct complex, structured inputs without custom engineering. This unlocks more advanced use cases and tighter integrations.

The `structured-chat-zero-shot-react-description` agent provides this functionality out-of-the-box. Define tools with proper `args_schema`, then build agents that can use them in powerful ways.


# Structured Tool Chat Agent

## Overview

The structured tool chat agent can utilize multiple tools using their `args_schema` to populate the action input. This allows more complex multi-tool interactions compared to agents that take a single string action input.

## Configuration

Import required modules:

```python
from langchain.agents import AgentType  
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
```

Initialize tools - here we use a browser, Google Sheets, and a SQL database:

```python
browser_toolkit = PlaywrightBrowserToolkit(...)
spreadsheet_toolkit = GoogleSheetsToolkit(...)
sql_toolkit = PostgresToolkit(...)
tools = browser_toolkit.get_tools() + spreadsheet_toolkit.get_tools() + sql_toolkit.get_tools() 
```

Initialize the agent with the tools:

```python 
agent = initialize_agent(tools, llm, agent_type=AgentType.STRUCTURED_TOOL_CHAT)
```

## Usage

Call the agent to take multi-tool actions:

```python
response = await agent.run("Browse to example.com, add the page title to my spreadsheet, and insert the URL into my database")
```

The agent will use the tools' `args_schema` to populate the action input.

## Examples

### Web Scraping and Data Storage

Scrape a website and store data in a database:

```python
input = "Browse to example.com, extract the page text, and store it in my database"
response = await agent.run(input)
```

The agent will:

1. Navigate to the website using the browser tool
2. Extract the page text using the browser tool 
3. Insert the text into the configured database using the SQL tool

### Web Automation and Spreadsheets

Automate form submissions and track data in a spreadsheet:

```python
input = "Go to example.com/form, fill in the form fields with my details, submit it, and add the submission timestamp to my spreadsheet" 
response = await agent.run(input)
```

The agent will:

1. Navigate to the form using the browser tool
2. Populate the form fields using the browser tool
3. Submit the form using the browser tool
4. Add the submission timestamp to the configured spreadsheet using the Google Sheets tool


### Complex Orchestration

Chain together actions across all tools:

```python
input = "Browse to example.com, extract the links, store them in my database, add the link count to my spreadsheet, and summarize the page content"
response = await agent.run(input) 
```

## How args_schema populates the action input

The `args_schema` defined by each tool specifies the required parameters. For example:

```python
# Browser tool args_schema
browser_args_schema = {"url": "The URL to navigate to"} 

# Spreadsheet tool args_schema
spreadsheet_args_schema = {"text": "The text to add", "cell": "The cell reference"}

# SQL tool args_schema 
sql_args_schema = {"text": "The text to insert", "table": "The table name"}
```

The agent uses these schemas to populate the action input:

```python
# Action input for browser tool
action_input = {"action": "navigate_browser", 
                "action_input": {"url": "https://example.com"}}

# Action input for spreadsheet tool                 
action_input = {"action": "add_text_cell",
                "action_input": {"text": "Timestamp", "cell": "A1"}}

# Action input for SQL tool
action_input = {"action": "insert_text_table",
                "action_input": {"text": "Page content", "table": "pages"}}
```

## Conclusion

The structured tool chat agent enables complex orchestration and automation by using multiple tools and their args_schemas. This is an improvement over single action string agents. The agent makes it easy to chain together multi-step workflows across diverse tools.


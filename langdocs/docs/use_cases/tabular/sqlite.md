

# SQLDatabaseChain 

The `SQLDatabaseChain` allows answering natural language questions by querying a SQL database. It converts the question to SQL, runs against the database, and returns the result.

## Installation and Setup

To use the chain, first install LangChain and SQLAlchemy:

```
pip install langchain sqlalchemy
```

Then create an SQLAlchemy engine and initialize the `SQLDatabase` utility:

```python
from sqlalchemy import create_engine  
from langchain.utilities import SQLDatabase

engine = create_engine('sqlite:///mydatabase.db')
db = SQLDatabase(engine)
```

## Basic Usage

Pass the `SQLDatabase` and an LLM to initialize the chain:

```python
from langchain import OpenAI
from langchain.chains.sql_database import SQLDatabaseChain  

llm = OpenAI()
chain = SQLDatabaseChain(llm, db) 

result = chain("How many users are in the database?")
print(result)
```

The chain handles the full loop - translating the question to SQL, querying the database, and returning the result.

## Customizing the Prompt

The prompt can be customized to provide the LLM more context on the database schema:

```python 
prompt = PromptTemplate(
  input_variables=["question", "table_info"],
  template="Answer the {question} using the database schema below: {table_info}"
)

table_info = "\n".join([table.ddl for table in db.metadata.tables.values()])

chain = SQLDatabaseChain(llm, db, prompt=prompt, table_info=table_info)
```

Table info and sample rows can also be configured in `SQLDatabase`.

## Advanced Usage

For more control, `return_intermediate_steps` returns the generated SQL and query result:

```python
chain = SQLDatabaseChain(llm, db, return_intermediate_steps=True)
result = chain("How many users are in the database?")
print(result.intermediate_steps) 
```

The `use_query_checker` option attempts to fix invalid SQL before executing: 

```python
chain = SQLDatabaseChain(llm, db, use_query_checker=True) 
```

## Conclusion

The `SQLDatabaseChain` provides a simple way to leverage large language models to query databases in natural language. With the ability to customize the prompt and output, it can be adapted to many use cases.




# Structured Output Parser

The structured output parser allows returning multiple text fields from a language model response. While more advanced parsers like the Pydantic parser exist, the structured output parser is useful for simple text-only responses when you need multiple fields.

## Introduction

Structured output parsers allow parsing language model responses into multiple fields. This is useful when you want to retrieve structured data instead of just a text response. The structured parser is simple and lightweight, making it a good choice for basic text responses.

## Overview

The structured output parser works by:

1. Defining a schema for the desired response structure using `ResponseSchema` objects. Each schema has a `name` and `description`.

2. Creating the parser by passing the schema to `StructuredOutputParser.from_response_schemas()`. 

3. Getting formatting instructions from the parser using `get_format_instructions()` and injecting them into the prompt template.

4. Calling the language model with the formatted prompt.

5. Parsing the language model response using `output_parser.parse()` to return a structured output.

## Usage Examples

### Basic Usage

Here is basic usage with a language model:

```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

response_schemas = [
  ResponseSchema(name="answer", description="answer to the user's question"),
  ResponseSchema(name="source", description="source for the answer"), 
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

prompt_template = "Answer the question: {question}\n{format_instructions}"

prompt = PromptTemplate(
  template=prompt_template,
  input_variables=["question"],
  partial_variables={"format_instructions": parser.get_format_instructions()}  
)

# Call model and parse response
output = parser.parse(model(prompt.format(question="What is the capital of France?")))

print(output) 
# {'answer': 'Paris', 'source': 'Wikipedia'} 
```

### Usage with Chat Models

The structured parser can also be used with chat models:

```python
import langchain

# Set up parser  
parser = StructuredOutputParser(...)

# Create chat prompt template
prompt = langchain.ChatPromptTemplate(
  messages=[
    langchain.HumanMessage(...)    
  ],
  input_variables=["question"],
  partial_variables={"format_instructions": parser.get_format_instructions()}  
)

# Call chat model and parse response
output = parser.parse(chat_model(prompt.format(...)).content) 
```

### Usage with Multiple Input Variables

Here is an example with multiple input variables:

```python
response_schemas = [
  ResponseSchema(name="summary", description="summary of the book"),
  ResponseSchema(name="author", description="author of the book"),
  ResponseSchema(name="year", description="year the book was published"),  
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

prompt_template = """
Provide the following information about the book: {title} by {author}:  
{format_instructions}
"""

prompt = PromptTemplate(
  template=prompt_template,
  input_variables=["title", "author"],
  partial_variables={"format_instructions": parser.get_format_instructions()}
)

output = parser.parse(model(prompt.format(title="The Great Gatsby", author="F. Scott Fitzgerald")))

print(output)
# {'summary': 'The Great Gatsby...', 'author': 'F. Scott Fitzgerald', 'year': '1925'}
```

### Usage with a Complex Schema

This shows usage with a more complex schema:

```python
response_schemas = [
  ResponseSchema(name="title", description="title of the film"),
  ResponseSchema(name="release_year", description="release year of the film"),
  ResponseSchema(name="actors", description="list of actors in the film"),
  ResponseSchema(name="plot_summary", description="brief plot summary of the film"),
]  

parser = StructuredOutputParser.from_response_schemas(response_schemas)

prompt_template = """
Provide details about the film {title}: 
{format_instructions}
"""

output = parser.parse(model(prompt.format(title="The Matrix")))  

print(output)
# {
#   'title': 'The Matrix',
#   'release_year': '1999',
#   'actors': ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],  
#   'plot_summary': 'A computer hacker learns that reality is an illusion...' 
# }
```

### Usage in a Python Framework

Here is an example of using the parser in a Python web framework like FastAPI:

```python
from fastapi import FastAPI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema  

app = FastAPI()

@app.post("/summarize")  
def summarize(text: str):
  response_schemas = [
    ResponseSchema(name="summary", description="summary of the text"),
  ]
  
  parser = StructuredOutputParser.from_response_schemas(response_schemas) 
  
  prompt = f"Summarize this text: {text}\n{parser.get_format_instructions()}"

  output = parser.parse(model(prompt))

  return output
```

## Troubleshooting Parsing Failures

Here are some common parsing failures and how to troubleshoot them:

**Schema name mismatch** - The parsed response must match the defined schema names exactly. Double check for typos or inconsistencies.

**Incorrect formatting** - The response must follow the provided formatting instructions. Verify the instructions are being inserted in the prompt correctly.

**Missing fields** - All fields in the defined schema must exist in the parsed response. The model may have failed to generate the full response. Try rephrasing the prompt or using different examples.

**Other parsing errors** - Look at the full error trace - it often provides hints on what went wrong. The error may come from the parser itself or downstream code consuming the parsed output.

## Conclusion

The structured output parser provides a simple way to get multiple text fields from language model responses. While basic, it is easy to use and avoids needing more complex parsers when only text outputs are required. Properly formatting prompts and handling potential parsing failures are key to using structured output parsers effectively.


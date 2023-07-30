

# Output Parsers

Output parsers are classes that help structure language model responses into more usable formats. They allow extracting structured data like JSON, key-value pairs, lists, etc from unstructured text.

## Overview

There are two main methods an output parser must implement:

- `get_format_instructions`: Returns instructions for how the LM output should be formatted.
- `parse`: Parses text into a structured format.

There is also one optional method:

- `parse_with_prompt`: Parses text using the original prompt. 

Output parsers provide a bridge between raw language model text and structured data formats.

## Common Output Parsers

### Pydantic Parser

This parser formats output into a Pydantic model object.

You define a Pydantic model class specifying the desired fields and types:

```python
from pydantic import BaseModel, Field

class Actor(BaseModel):
  name: str 
  films: List[str]
```

Then create a parser instance, passing the model:

```python
parser = PydanticOutputParser(pydantic_object=Actor)
```

You can parse text into the Pydantic object:

```python
text = '{"name": "Tom Hanks", "films": ["Forrest Gump", "Cast Away"]}'

actor = parser.parse(text)
print(actor.name)
# "Tom Hanks"
```

Pydantic also supports validation. You can define custom validators:

```python
from pydantic import validator

@validator('name')  
def name_must_contain_space(cls, name):
  if ' ' not in name:
    raise ValueError('Name must contain space')
  return name
```

Invalid parses will raise errors:

```python 
text = '{"name": "TomHanks", "films": ["Forrest Gump"]}'

try:
  actor = parser.parse(text) 
except ValueError as e:
  print(e)
  # Name must contain space
```

### Structured Parser

This parser extracts specific fields.

Define the desired fields:

```python
schemas = [
  ResponseSchema(name="title", description="title of book"),
  ResponseSchema(name="author", description="author of book")
]

parser = StructuredOutputParser(schemas=schemas)
```

Then parse text:

```python
text = "title: The Great Gatsby\nauthor: F. Scott Fitzgerald"

parsed = parser.parse(text) 
# {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
```

### List Parser

This parser extracts a comma-separated list.

```python
parser = CommaSeparatedListOutputParser()

text = "apples, bananas, oranges" 

parsed = parser.parse(text)
# ['apples', 'bananas', 'oranges']
```

### Auto-Fixing Parser

This parser tries to fix formatting errors using a language model.

It takes another parser and a language model:

```python
original_parser = StructuredOutputParser(...)
llm = MyLLM() 

fixing_parser = OutputFixingParser(
  parser=original_parser,
  llm=llm  
)
```

If the original parser fails, it calls the LLM to fix the output:

```python
invalid_text = "invalid output"

fixed_text = fixing_parser.parse(invalid_text)
```

The LLM will get the invalid text and formatting instructions to generate a corrected output that the original parser can parse.

This helps handle situations where the language model returns malformed output.

## Conclusion

LangChain provides common output parsers like Pydantic, Structured, List and Auto-Fixing to extract structured data from language model text. The parsers can be used independently or composed together. Refer to the documentation for more details and examples.


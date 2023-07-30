

# List Parser

The ListParser is an output parser in LangChain that parses language model responses into Python lists of comma-separated values. It implements the core `parse` and `get_format_instructions` methods required of LangChain output parsers.

## Overview

The ListParser provides a simple way to get structured lists back from language model responses. It is commonly used when you want the language model to return a list of items based on some prompt. 

Some examples of when the ListParser is useful:

- Getting a list of movie recommendations
- Getting a list of ingredients for a recipe
- Getting a list of pros/cons for a product

## Usage

Here is a typical workflow for using the ListParser:

1. Import the ListParser and create an instance:

```python
from langchain.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()
```

2. Get the format instructions from the parser to include in your prompt:

```python
format_instructions = parser.get_format_instructions() 
```

3. Include the format instructions in your prompt template:

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
  template="List 3 ice cream flavors: {format_instructions}",
  partial_variables={"format_instructions": format_instructions}
)
```

4. Send the prompt to your language model and parse the response:

```python 
from langchain.llms import OpenAI

llm = OpenAI()  
response = llm.predict(prompt.to_string())

parsed = parser.parse(response)
# ['Vanilla', 'Chocolate', 'Strawberry'] 
```

The ListParser works with any LangChain compatible language model, including `OpenAI` for standard models and `ChatOpenAI` for chat models.

## Handling Invalid Responses

If the language model returns a response that is not a valid comma-separated list, the ListParser will fail to parse it.

To handle invalid responses, the `OutputFixingParser` can be used. It takes the invalid response and format instructions and asks the language model to fix the formatting:

```python
from langchain.output_parsers import OutputFixingParser

fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())

invalid_response = "Vanilla, Chocolate, Strawberry"

fixed = fixing_parser.parse(invalid_response) 
# ['Vanilla', 'Chocolate', 'Strawberry']
```

## Summary

The ListParser provides an easy way to get Python lists back from language models. It can be used directly or with the OutputFixingParser to handle invalid responses. The parser works seamlessly with prompt templates to inject formatting instructions.


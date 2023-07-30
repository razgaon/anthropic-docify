

# LLMChain

## Overview

The LLMChain is a core building block in LangChain that bundles together a prompt template and a language model into a simple chain. It formats the prompt template using provided input values, queries the language model, and returns the response.

## How it Works

An LLMChain consists of two key components:

- A PromptTemplate that defines the prompt structure and input variables  
- A language model (LLM or chat model) that generates the response

The LLMChain formats the prompt template with the provided input values (and memory if enabled). It then sends the prompt to the language model and returns the raw response.

## Usage Example

Here is an example of initializing an LLMChain from a PromptTemplate and LLM:

```python
from langchain import PromptTemplate, OpenAI, LLMChain

prompt_template = PromptTemplate(
  input_variables=["product"],
  template="What is a good name for a company that makes {product}?"
)

llm = OpenAI() 
llm_chain = LLMChain(
  llm=llm,
  prompt=prompt_template  
)

print(llm_chain.run("colorful socks"))
```

This will format the prompt with "colorful socks" and send it to the LLM, returning something like "Colorful Feet Inc."

## Key Features

### Memory

LLMChains can utilize memory to maintain conversation context across prompts. This allows an agent to remember facts and refer back to previous statements.

Memory can be enabled like:

```python 
llm_chain = LLMChain(
  ...,
  memory=RedisMemory() 
)
```

### Flexible Execution 

In addition to `__call__` and `run`, LLMChains provide other ways to execute the chain:

- `apply` - Run against a list of inputs and return a list of outputs
- `generate` - Like `apply` but returns an LLMResult with metadata
- `predict` - Specify inputs as kwargs rather than a dict

### Built-in Parsing

Use `predict_and_parse` and `apply_and_parse` to apply the prompt's output parser to the LLM response. This parses the output to a structured format.

### Initialization

LLMChains can be constructed from a prompt template and LLM directly, or from a string template.

## Conclusion

The LLMChain provides a simple abstraction for combining a prompt template and language model into a reusable component. Its flexibility through methods like `apply` and built-in parsing make it a versatile building block for LangChain applications.


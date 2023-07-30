

# Prompt Templates

Prompt templates provide a reproducible and customizable way to generate prompts for language models. They allow passing in parameters from the user to generate prompts on the fly. LangChain offers prompt templates tailored for both LLM (large language models) and chat models.

## Overview

A prompt template contains: 

- A template string with placeholders (e.g. `{product}`)
- A list of input variable names (e.g. `["product"]`)  

To generate a prompt, you pass in values for the input variables. The template string is formatted with those values to create the final prompt.

For example:

```python
template = "What is a good name for a company that makes {product}?"
prompt = PromptTemplate(template=template, input_variables=["product"])

prompt.format(product="shoes")
# "What is a good name for a company that makes shoes?"
```

## PromptTemplate

The `PromptTemplate` class is used for LLM models like GPT-3. It takes a template string and generates a text prompt.

A prompt template can contain:

- Instructions to the language model
- A few shot examples  
- A question to the language model

For example:

```python 
template = """
You are a naming expert. The company wants a fun, catchy name. 

Here are example names you have generated:
For a pet store: Pawsome Pets
For a shoe store: Kicks R Us

What is a good name for a company that makes {product}? 
"""

prompt = PromptTemplate(template=template, input_variables=["product"])

prompt.format(product="socks")
```

You can create a `PromptTemplate` directly from a template string using `PromptTemplate.from_template()`. The input variables will be parsed automatically.

## ChatPromptTemplate

The `ChatPromptTemplate` class is used for chat models like the OpenAI Chat API. Chat models take in a list of message objects rather than raw text.

`ChatPromptTemplate` allows you to create templates for messages with different roles like system, assistant, and user. 

For example:

```python
system_template = "You are an AI assistant fluent in {language}."
system_prompt = SystemMessagePromptTemplate(
  template=system_template,
  input_variables=["language"]  
)

user_template = "{text}" 
user_prompt = HumanMessagePromptTemplate(
  template=user_template,
  input_variables=["text"]
)

chat_prompt = ChatPromptTemplate(
  system_prompt, user_prompt  
)

chat_prompt.format(
  language="French",
  text="What is your name?"
)
```

This allows you to fully leverage chat models by providing role-based instructions.

## Best Practices

Here are some tips for writing effective prompt templates:

- Frame instructions clearly  
- Provide 2-3 diverse examples 
- Ask focused questions
- Adjust temperature if needed
- Test templates extensively

Investing in high quality templates will lead to better model performance.


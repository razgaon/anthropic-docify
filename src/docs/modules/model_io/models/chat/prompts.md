

# Prompts for Chat Models

Prompts are a key part of how chat models work. Unlike traditional language models that take raw text as input, chat models are designed to have a conversation and take a series of chat messages as input. 

Constructing effective prompts is crucial to get the most out of chat models. LangChain provides several classes to make building prompts for chat models easy.

## Overview

There are 3 main classes:

- `PromptTemplate`: Base class for creating parametrized prompt templates.
- `MessagePromptTemplate`: Creates a prompt template associated with a specific role like system, assistant, or human. 
- `ChatPromptTemplate`: Creates a full prompt made of `MessagePromptTemplate`s. Used to format prompts to pass to chat models.

## MessagePromptTemplate

A `MessagePromptTemplate` represents a single message in a conversation and is tied to a specific role. 

For example, you can create a template for a system message:

```python
template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message = SystemMessagePromptTemplate.from_template(template)
```

Or directly:

```python
prompt = PromptTemplate(
  template="You are a helpful assistant that translates {input_language} to {output_language}.",
  input_variables=["input_language", "output_language"]
)
system_message = SystemMessagePromptTemplate(prompt=prompt) 
```

Some common roles:

- `SystemMessagePromptTemplate`
- `AIMessagePromptTemplate`
- `HumanMessagePromptTemplate` 

### Example

Here is an example workflow creating a system message template:

```python
# Template 
template = "You are a helpful assistant that translates {input_language} to {output_language}."

# Create template
system_message = SystemMessagePromptTemplate.from_template(template)

# Format template 
formatted_message = system_message.format(
  input_language="English",
  output_language="French"  
)

print(formatted_message)

# You are a helpful assistant that translates English to French.
```

## ChatPromptTemplate

A `ChatPromptTemplate` represents a full conversation prompt made of `MessagePromptTemplate`s.

For example: 

```python 
system_message = SystemMessagePromptTemplate(...)
human_message = HumanMessagePromptTemplate(...)

chat_prompt = ChatPromptTemplate.from_messages([
  system_message,
  human_message
]) 
```

You can format the full prompt:

```python
formatted_messages = chat_prompt.format_prompt(
  input_language="English",
  output_language="French",
  text="I love programming."  
).to_messages()
```

And pass to a chat model:

```python
response = chat(formatted_messages)
```

### Example 

Full prompt formatting example:

```python
# System and human templates
system_template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

system_message = SystemMessagePromptTemplate.from_template(system_template)  
human_message = HumanMessagePromptTemplate.from_template(human_template)

# Chat template
chat_prompt = ChatPromptTemplate.from_messages([
  system_message,
  human_message
])

# Format prompt
formatted_messages = chat_prompt.format_prompt(
  input_language="English", 
  output_language="French",
  text="I love programming."
).to_messages() 

# Pass to chat model 
response = chat(formatted_messages)
```

## Summary 

The prompt classes in LangChain provide an easy way to construct prompts specifically for chat models. Key points:

- `MessagePromptTemplate` represents a single chat message
- `ChatPromptTemplate` represents a full conversation prompt
- Format templates using input variables 
- Convert formatted templates to chat messages to pass to models

Using these templates can help you fully leverage chat capabilities compared to just passing raw text.


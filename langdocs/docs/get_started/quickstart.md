

# Quickstart

## Installation

To install LangChain run:

* Pip  
* Conda

```
pip install langchain
```

```
conda install langchain -c conda-forge
```

For more details, see our [Installation guide](/docs/get_started/installation.html).

## Environment setup

Using LangChain will usually require integrations with one or more model providers, data stores, APIs, etc. For this example, we'll use OpenAI's model APIs.

First we'll need to install their Python package:

```
pip install openai
```

Accessing the API requires an API key, which you can get by creating an account and heading [here](https://platform.openai.com/account/api-keys). Once we have a key we'll want to set it as an environment variable by running:

```
export OPENAI_API_KEY="..." 
```

If you'd prefer not to set an environment variable you can pass the key in directly via the `openai_api_key` named parameter when initiating the OpenAI LLM class:

```python
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="...")
```

## Building an application

Now we can start building our language model application. LangChain provides many modules that can be used to build language model applications. Modules can be used as stand-alones in simple applications and they can be combined for more complex use cases.

The core building block of LangChain applications is the LLMChain. This combines three things:

- LLM: The language model is the core reasoning engine here. In order to work with LangChain, you need to understand the different types of language models and how to work with them.
- Prompt Templates: This provides instructions to the language model. This controls what the language model outputs, so understanding how to construct prompts and different prompting strategies is crucial. 
- Output Parsers: These translate the raw response from the LLM to a more workable format, making it easy to use the output downstream.

In this getting started guide we will cover those three components by themselves, and then cover the LLMChain which combines all of them. Understanding these concepts will set you up well for being able to use and customize LangChain applications. Most LangChain applications allow you to configure the LLM and/or the prompt used, so knowing how to take advantage of this will be a big enabler.

## LLMs

There are two types of language models in LangChain:

- **LLMs**: Language models that take a string as input and return a string as output.
- **ChatModels**: Language models that take a list of messages as input and return a message as output. 

The input/output for LLMs is simple - just a string in and out. But ChatModels are more complex. The input is a list of `ChatMessage` objects, and the output is a single `ChatMessage` object.

A `ChatMessage` has two required components:

- `content`: The content text of the message
- `role`: The role of the sender, like `"user"`, `"assistant"`, etc.

LangChain provides several predefined roles:

- `HumanMessage`: A `ChatMessage` from a human/user.   
- `AIMessage`: A `ChatMessage` from an AI/assistant.
- `SystemMessage`: A `ChatMessage` from the system.
- `FunctionMessage`: A `ChatMessage` from a function call.

There is also a generic `ChatMessage` class you can use to define custom roles. 

Understanding the difference between LLMs and ChatModels is key to constructing effective prompts. See our [prompting guide](/docs/guides/prompting.html) for more details.

The standard interface LangChain exposes for both types has two methods:

- `predict`: Takes a string, returns a string
- `predict_messages`: Takes a list of messages, returns a message

Let's see some examples:

```python
from langchain.llms import OpenAI  
from langchain.chat_models import ChatOpenAI
  
llm = OpenAI()  
chat_model = ChatOpenAI()
  
llm.predict("hi!")  
# "Hi"
  
chat_model.predict("hi!")
# "Hi" 
```

We can pass parameters like `temperature` when initializing the models.

Using `predict`:

```python 
text = "What would be a good company name for a company that makes colorful socks?"
  
llm.predict(text)
# "Feetful of Fun"
  
chat_model.predict(text)  
# "Socks O'Color"
```

Using `predict_messages`:

```python
from langchain.schema import HumanMessage
  
text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]
  
llm.predict_messages(messages)
# "Feetful of Fun"
  
chat_model.predict_messages(messages) 
# "Socks O'Color"
```

## Prompt Templates

Most LLM applications don't pass user input directly to the model. Instead, they add the input to a prompt template that provides context. 

For example, our previous company name prompt contained instructions to the model:

```
"What would be a good company name for a company that makes colorful socks?"
```

It would be better if the user only had to provide the company description, without formatting instructions. 

This is what prompt templates help with! They bundle up the logic to go from user input to a full prompt.

A simple example:

```python
from langchain.prompts import PromptTemplate
  
template = "What is a good name for a company that makes {product}?"
prompt = PromptTemplate.from_template(template)

prompt.format(product="colorful socks")
```

Outputs:

```
"What is a good name for a company that makes colorful socks?" 
```

The key advantages of prompt templates:

- Partial formatting - format just some variables 
- Composition - easily combine templates
- Message formatting - make prompts with different message types and roles

For more details, see the [prompting guide](/docs/guides/prompting.html).

## Output Parsers  

Output parsers convert the raw LLM output into a usable format. 

Some examples:

- LLM text -> structured data like JSON
- Chat message -> just the message content 
- Extra info from API call -> string

We can write a custom parser to turn a comma separated list into a Python list:

```python
from langchain.schema import BaseOutputParser

class CommaSeparatedListParser(BaseOutputParser):

  def parse(self, text):
    return text.split(", ")

parser = CommaSeparatedListParser()
parser.parse("hi, there, friend")
# ['hi', 'there', 'friend']
```

See the [output parser guide](/docs/guides/output_parsing.html) for more examples.

## LLMChain

We can combine a prompt, LLM, and parser into a chain:

```python
from langchain import PromptTemplate, OpenAI, LLMChain

prompt = PromptTemplate("What is a good name for a company that makes {product}?")
llm = OpenAI()
parser = CommaSeparatedListParser() 

chain = LLMChain(
  prompt=prompt,
  llm=llm,
  output_parser=parser  
)

chain.run(product="shoes")
```

The chain handles:

- Formatting the prompt
- Calling the LLM
- Parsing the output

Making it easy to run LLMs for different applications.

We can customize each component as needed. The [chains guide](/docs/guides/chains.html) covers customization and advanced usage in more detail.

## Conclusion

In this quickstart we covered:

- Installing LangChain
- LLMs vs ChatModels 
- Prompt Templates
- Output Parsers
- Constructing LLMChains

This provides a foundation for building custom chains and agents.

To continue:

- Dive deeper into the [core modules](/docs/modules)  
- Check out [end-to-end use cases](/docs/use_cases)
- Join the [community](https://github.com/hwchase17/langchain) to meet other developers!




# Getting Started with LangChain

LangChain provides building blocks for creating applications powered by language models. This guide will walk you through installing LangChain, setting up your environment, and building a simple "Hello World" application.

## Installation

To install LangChain, run:

```
pip install langchain
```

LangChain requires Python 3.7+.

## Authentication

Before using LangChain, you'll need access to a language model API. LangChain supports both text-based LLMs like GPT-3 and chat-based models like Claude. You will need to acquire API keys for the specific model(s) you want to use. Refer to the documentation for each model for instructions on signing up and getting API credentials.

## Environment Setup

With API credentials in hand, you can now configure LangChain to use your desired models. The [LLM](/docs/modules/model_io/models/llms/) and [Chat](/docs/modules/model_io/models/chat/) model interfaces allow passing API keys and settings to instantiate a client. For example:

```python
from langchain.llms import OpenAI

openai_api_key = "YOUR_API_KEY" 

llm = OpenAI(api_key=openai_api_key)
```

## Hello World

Here is a simple LangChain script that generates text using GPT-3:

```python
from langchain import LLMChain, PromptTemplate

prompt = PromptTemplate(
    input="Hello world!",
    output="Hello to you too!"  
)

chain = LLMChain(
    llm="text-davinci-003",
    prompt=prompt
)

print(chain.run())
```

This script:

1. Defines a prompt template with an input and desired output.
2. Creates an LLMChain using GPT-3's davinci model.
3. Runs the chain, printing the generated text.

The output should be a friendly "Hello to you too!" message.

## Next Steps

You now have LangChain installed and authenticated, and can build simple applications! Next up:

- Learn more about [LLMs](/docs/modules/model_io/models/llms/) and [chat models](/docs/modules/model_io/models/chat/)  
- Build chains using different [modules](/docs/modules)
- Follow our [guides](/docs/guides) for end-to-end examples  
- Browse [use cases](/docs/use_cases) for inspiration




# Chat Models

Chat models are a type of language model optimized for conversational interactions. While they utilize standard language models under the hood, chat models expose a different interface than traditional LLMs. Rather than a simple "text in, text out" API, chat models are designed to take in and return conversational "messages" - making them ideal for chatbots and digital assistants.

## Key Differences from LLMs

LLMs (large language models) are optimized for free-form text completion given a single prompt. They take a prompt string as input and return a completed text string. 

Chat models differ in a few key ways:

- **Input**: Instead of a single text prompt, chat models are designed to take a **list of messages** as input. These messages contain **speakers** like "System", "Assistant", and "Human" to provide conversational context.

- **Output**: Rather than outputting raw text, chat models return a full conversational **message** as output, usually from the "Assistant" speaker.

- **Conversational context**: Chat models are optimized to maintain conversational context across multiple turns. LLMs generate independent completions without awareness of previous context.

## Getting Started with Chat Models in LangChain

To start using chat models, first install the OpenAI Python package:

```python
pip install openai
```

Then create an instance of the `ChatOpenAI` class:

```python 
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI()
```

### Making Predictions

You can get predictions by passing a list of messages:

```python
from langchain.schema import HumanMessage, AIMessage  

messages = [
  HumanMessage("Hello there!"), 
  AIMessage("Hi, how can I help you today?"),
  HumanMessage("I'm looking for a good restaurant nearby."),
  AIMessage("What type of cuisine are you interested in?")
]

response = chat(messages)
print(response)
# AIMessage(content="Here are some top rated Italian restaurants nearby...", ...)
```

`chat()` returns a conversational `AIMessage` response.

You can also call `generate()` to get multiple candidate responses:

```python 
result = chat.generate(messages)
print(result.generations[0][0].text)
# "Here are some great Italian restaurants within 10 miles..."
```

### Maintaining Conversational State

A key strength of chat models is their ability to maintain conversational context across multiple turns:

```python
messages = [
  SystemMessage("You are a helpful assistant."),
  HumanMessage("What is the weather forecast for tomorrow?"),
  AIMessage("The weather forecast for tomorrow is sunny with a high of 70F."),
  HumanMessage("What about the day after tomorrow?"),
]

response = chat(messages)
# AIMessage(content="The forecast for the day after tomorrow is partly cloudy with a high of 65F.") 
```

## Conclusion

Chat models provide a natural conversational interface by taking in and returning chat messages. Under the hood they utilize LLMs, but the message-based API makes them easy to integrate for chatbots. LangChain provides a simple interface to leading chat models like OpenAI's ChatGPT through the `ChatOpenAI` class.


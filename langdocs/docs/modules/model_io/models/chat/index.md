

# Chat Models

## Overview

Chat models are a type of language model optimized for conversational interactions. While regular language models take a text prompt and return a text completion, chat models take a list of conversational messages as input and output a conversational response.

Chat models use language models under the hood but expose a different interface. As mentioned in the FAQ, the key difference is that chat models take chat messages as input and output, rather than raw text strings like regular language models.

Some examples of chat models are Claude (Anthropic), GPT-4 (Anthropic), and the OpenAI Chat model. Chat models are commonly used for conversational agents and chatbots.

## Getting Started

To start using chat models in LangChain, first install the OpenAI Python package:

```
pip install openai
```

Then load a chat model instance:

```python
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
```

## Chat Message Interface

As explained in the FAQ, the chat model interface is based on exchanging chat messages rather than raw text. The main message types are:

- `HumanMessage`: Message from the user  
- `AIMessage`: Message from the AI assistant
- `SystemMessage`: Setup prompt for the AI assistant

You can pass these as a list to the chat model to get a conversational response:

```python
from langchain.schema import HumanMessage, AIMessage

messages = [
  SystemMessage("You are an AI assistant fluent in French and English"), 
  HumanMessage("What is your name?")
]

response = chat_model(messages)
# AIMessage(content="My name is Claude.") 
```

As noted in the FAQ, OpenAI's chat model supports multiple messages as input. You can pass a conversation history to get a context-aware response:

```python
messages = [
  SystemMessage("You are a helpful assistant that translates English to French."),
  HumanMessage("I love programming."),
  HumanMessage("What is your name?")
]

response = chat_model(messages)
```

## Batch Processing

You can generate responses for multiple sets of messages using the `generate` method, as mentioned in the FAQ. This returns a `LLMResult` object with additional metadata:

```python 
batch_messages = [
  [
    SystemMessage("You are a helpful assistant that translates English to French."),
    HumanMessage("I love programming.")
  ],
  [...]
]

result = chat_model.generate(batch_messages)
```

The `LLMResult` contains the chat message responses as well as usage statistics and other metadata.

See the [full chat model documentation](/docs/modules/model_io/models/chat/) for more details on advanced usage.


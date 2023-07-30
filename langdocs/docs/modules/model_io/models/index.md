

# Language Models in LangChain

LangChain provides interfaces and integrations for two main types of language models: LLMs (Large Language Models) and Chat Models. Understanding the difference between these two types of models is key to using LangChain effectively.

## LLMs

LLMs (Large Language Models) are models that take a text string as input and return a text string as output. Examples include GPT-3, GPT-3.5, Codex. 

To use an LLM in LangChain:

```python
from langchain.llms import OpenAI

llm = OpenAI()

output = llm.predict("What is the capital of France?")
```

The `predict` method takes a string prompt and returns the model's generated string response.

## Chat Models

Chat models are tuned for having conversations. Their provider APIs take a list of chat messages as input rather than a single string. The messages are labeled with a speaker role, like "Human", "AI", or "System". The model returns a response chat message.

Examples of chat models include Claude, GPT-4, and Anthropic's conversational model.

To use a chat model in LangChain:

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat_model = ChatOpenAI() 

messages = [HumanMessage("What is the capital of France?")]
response = chat_model.predict_messages(messages)
```

The `predict_messages` method takes a list of `ChatMessage` objects and returns a `ChatMessage` response.

## Chat Messages

When working with chat models, inputs and outputs are `ChatMessage` objects. These contain:

- `content`: The text content of the message
- `role`: The speaker role, like "Human" or "AI" 

LangChain provides helper classes for common roles:

- `HumanMessage`: Message from a human
- `AIMessage`: Message from an AI assistant
- `SystemMessage`: Message from the system

## Summary

In summary, LLMs take string input and output while Chat Models take chat messages as input and output. LangChain provides interfaces for both, but understanding this key difference is important for using the library effectively. The helper classes like `HumanMessage` and `AIMessage` make working with Chat Models easy.


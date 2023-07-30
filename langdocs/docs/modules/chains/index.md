

# Chains

Chains are a key concept in LangChain that allow combining multiple components together to build complex applications. At a high level, a chain takes some input, passes it through a series of components like LLMs and parsers, and returns the final output. 

## Why Chains are Needed

Chains are needed for several reasons:

- **Modularity** - They allow breaking down complex logic into reusable components
- **Simplified Debugging** - Each component can be tested in isolation  
- **Flexibility** - Components can be swapped in and out easily
- **Prompt Engineering** - Chains make it easy to shape the context and prompt seen by the LLM

Without chains, applications would need large monolithic functions that are hard to maintain. 

## Getting Started with Chains

The simplest chain is the `LLMChain`. It combines:

- A language model (LLM) 
- A prompt template 
- Optionally, an output parser

Here is a simple example:

```python
from langchain import PromptTemplate, OpenAI, LLMChain

prompt = PromptTemplate(
  template="What is a good name for a company that makes {product}?"
)

llm = OpenAI() 

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("colorful socks"))
```

This shows the power of chains - it abstracts away the prompt formatting, querying the LLM, and parsing the output into one simple call.

## ChatModels vs LLMs

A key difference is that ChatModels take a list of `ChatMessage` objects as input rather than just a string. For example:

```python 
from langchain import ChatOpenAI, HumanMessage

chat_model = ChatOpenAI()

messages = [
  HumanMessage(content="What is a good name for a company that makes colorful socks?")  
]

response = chat_model.predict_messages(messages)
print(response.content)
```

Understanding the difference between LLMs and ChatModels is important for constructing effective prompts.

## Summary

In summary, chains simplify combining components like LLMs, prompt templates, and parsers to build robust applications. They provide modularity, improved debugging, flexibility, and prompt engineering benefits.

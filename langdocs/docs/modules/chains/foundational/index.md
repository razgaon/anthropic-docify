

# Chains

Chains are a core concept in LangChain that allow combining multiple components like prompt templates, LLMs, and data connections into a single application flow. Chains provide a simple but powerful paradigm for creating modular and extensible NLP applications.

## Introduction

A chain is a sequence of calls to components, which can include other chains or more atomic building blocks like prompt templates and LLMs. The key benefits of chains are:

- **Modularity**: Complex flows can be broken down into reusable chains that can be composed together  
- **Extensibility**: It's easy to add new components like different LLMs into an existing chain
- **Maintainability**: Chains encapsulate logic, making it easier to debug and update applications
- **Flexibility**: Chains enable dynamic flows based on context and directives

The base `Chain` interface in LangChain is simple - it mainly requires implementing a `__call__` method. But this simple interface enables powerful applications when chains are composed.

## Foundational Chains 

LangChain comes with several foundational building block chains:

### LLMChain

The `LLMChain` is the most basic chain that formats a prompt template and calls an LLM. For example:

```python
from langchain import PromptTemplate, OpenAI, LLMChain

prompt_template = "What is a good name for a company that makes {product}?"

llm = OpenAI(temperature=0)  
llm_chain = LLMChain(
  llm=llm,
  prompt=PromptTemplate.from_template(prompt_template)  
)

llm_chain("colorful socks")
```

This chains together a prompt template and LLM into a simple application. The `LLMChain` allows easily incorporating an LLM into a modular chain architecture.

### RouterChain 

The `RouterChain` enables dynamically selecting the next chain based on context. For example:

```python
from langchain import RouterChain, LLMChain

llm_chain = LLMChain(...) 

router = RouterChain() 
router.add_route("weather", WeatherChain())
router.add_route("stocks", StocksChain())

router.run("what is the weather tomorrow?") # Runs WeatherChain
router.run("how are tech stocks doing?") # Runs StocksChain
```

This makes it possible to build adaptive flows that route differently based on user input.

### SequentialChain

The `SequentialChain` chains multiple calls together, piping the output of one as input to the next. For example:

```python
from langchain import SequentialChain, LLMChain

llm_chain1 = LLMChain(...)
llm_chain2 = LLMChain(...)

seq_chain = SequentialChain(llm_chain1, llm_chain2)

seq_chain("Hello!") 
# Runs llm_chain1, pipes output to llm_chain2
```

This enables creating multi-step conversational flows.

## How To Use Chains

Chains can be run by simply calling them like functions:

```python
chain("input")
```

They can also be composed by passing one chain into the initialization of another:

```python
chain2 = MyChain2(chain1=chain1) 
```

And they can be made stateful by adding a `Memory` object:

```python
from langchain.memory import Memory

memory = Memory()
chain = MyChain(memory=memory)
```

To learn more, see the [full documentation on chains](https://langchain.readthedocs.io/en/latest/modules/chains.html).


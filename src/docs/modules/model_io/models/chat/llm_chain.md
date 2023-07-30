

# LLMChain

LLMChain allows chaining together prompts and models to build simple yet powerful AI applications. This guide provides an overview of LLMChain and examples for getting started.

## Introduction

LLMChain is one of the core building blocks in LangChain. It chains together a prompt template and a language model to format prompts, query models, and return responses. 

Some key features:

- Supports both LLMs and chat models
- Easy formatting of prompts using input variables
- Flexible input methods including dicts, lists, and keywords  
- Additional options like `apply` for batch predictions

## Constructing an LLMChain

To use LLMChain, first create a `PromptTemplate` and a model.

```python
from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
  input_variables=["product"],
  template="What is a good name for a company that makes {product}?"  
)
```

Then construct the chain by passing the prompt and model.

```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt) 
```

## Passing Inputs

There are a few ways to pass inputs to an LLMChain:

**Dict**

```python
print(chain.run({"product": "colorful socks"}))
```

**Keywords** 

```python
print(chain.predict(product="colorful socks")) 
```

**List**

```python
inputs = [{"product": "socks"}, {"product": "shoes"}]
print(chain.apply(inputs))
```

## Additional Prediction Methods

LLMChain provides a few additional ways to run predictions:

- `apply` - Runs on a batch of inputs and returns a list of outputs
- `generate` - Returns a `LLMResult` with token usage and other metadata
- `predict` - Specifies inputs as keywords rather than a dict 

For example:

```python
inputs = [{"product": "socks"}, {"product": "computer"}]

outputs = chain.apply(inputs) # Returns list of outputs
result = chain.generate(inputs) # Returns LLMResult

chain.predict(product="shoes") # Keyword arguments
```

## Conclusion

In summary, LLMChain is a simple yet powerful building block that chains together prompts and models. It provides flexibility through multiple input methods, batch predictions, access to metadata, and easy composability into more complex chains.


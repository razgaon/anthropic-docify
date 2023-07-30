

# Sequential Chains

Sequential chains allow connecting multiple chains together into a pipeline that executes a sequence of steps. This is useful when you want to use the output of one chain as input to the next chain. There are two main types of sequential chains:

## SimpleSequentialChain 

The SimpleSequentialChain is the simplest sequential chain where each step has a single input and single output. The output of one step is passed directly as the input to the next step without needing to specify variable names.

```python
from langchain.chains import SimpleSequentialChain

chain1 = LLMChain(...)
chain2 = LLMChain(...)

pipeline = SimpleSequentialChain(chains=[chain1, chain2]) 
```

## SequentialChain

The SequentialChain allows for more flexibility by supporting multiple inputs and outputs at each step. This requires explicitly specifying input and output variable names to pass data between steps.

```python
from langchain.chains import SequentialChain

chain1 = LLMChain(..., output_key="summary")
chain2 = LLMChain(..., input_variables=["summary"]) 

pipeline = SequentialChain(
   chains=[chain1, chain2],
   input_variables=["text"],
   output_variables=["summary", "analysis"]  
)
```

## Variable Naming Best Practices

When connecting multiple chains, follow these tips for naming variables:

- Use descriptive names like "document_summary" rather than just "summary"
- Be consistent in naming across long pipelines
- Prefix variable names if passing between different components

## Managing State with Memory

Chaining many steps can require passing a lot of variables. The Memory classes provide ways to encapsulate state and minimize this.

### SimpleMemory

The SimpleMemory allows storing context to pass to later chains:

```python
memory = SimpleMemory(memories={"author": "James Joyce"}) 

pipeline = SequentialChain(
   ...,
   memory=memory
)
```

### KeyValueMemory 

The KeyValueMemory provides flexible storage and retrieval of context across chains:

```python
memory = KeyValueMemory()
memory.add("document", doc)

# Later retrieve value
doc = memory.get("document")
```

In summary, SequentialChain allows connecting multiple chains into a pipeline while Memory helps manage shared state between chains. Careful use of naming and memory minimization strategies helps build robust pipelines.


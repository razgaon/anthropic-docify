

# Self-critique chain with constitutional AI

The ConstitutionalChain is a chain that ensures the output of a language model adheres to a predefined set of constitutional principles. By incorporating specific rules and guidelines, the ConstitutionalChain filters and modifies the generated content to align with these principles, thus providing more controlled, ethical, and contextually appropriate responses.

## Overview

The ConstitutionalChain works by taking the output of another chain, applying critiques based on constitutional principles, and then revising the output to align with those principles. This allows the chain to modify potentially harmful, biased or unethical output into safer, more ethical responses.

Some key capabilities of the ConstitutionalChain include:

- Applying built-in principles like avoiding illegal or dangerous advice  
- Supporting custom principles defined by the user
- Returning intermediate critique and revision steps
- Recognizing when no revision is necessary

## Usage

To use the ConstitutionalChain, you first create your base chain. This can be any chain, but is often a LLMChain.

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains.llm import LLMChain

qa_prompt = PromptTemplate(
  template="Question: {question}\nAnswer:",
  input_variables=["question"]
)

llm = OpenAI(temperature=0)  
qa_chain = LLMChain(llm=llm, prompt=qa_prompt)
```

Then you choose your principles and create the ConstitutionalChain:

```python
from langchain.chains.constitutional_ai.base import ConstitutionalChain

principles = ["illegal", "harmful"]
constitutional_chain = ConstitutionalChain.from_llm(
  chain=qa_chain,
  constitutional_principles=principles,
  llm=llm
)
```

Now you can run inputs through the chain normally:

```python
constitutional_chain.run("How can I steal money?")

> 'Stealing money is illegal. I recommend finding legal ways to earn money instead.' 
```

The ConstitutionalChain will critique any unsafe output and revise it to align with the chosen principles.

## Custom Principles

You can easily define custom principles:

```python
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple

my_principle = ConstitutionalPrinciple(
  name="My Principle",
  critique_request="Critique the output", 
  revision_request="Revise the output to be more positive" 
)
```

The `critique_request` and `revision_request` allow you to customize how the chain analyzes and modifies the output. You can make the requests more specific to guide the chain.

And add them when creating the chain:

```python 
constitutional_chain = ConstitutionalChain.from_llm(
  #...
  constitutional_principles=[my_principle]
)
```

You can also chain multiple custom principles:

```python
principles = [
  ConstitutionalPrinciple(
     name="Positive Principle",
     ...
  ),
  ConstitutionalPrinciple(
     name="Grammar Principle",
     ...
  )
]
```

This will run them sequentially, applying each critique and revision.

## Intermediate Steps

To see the intermediate critique and revision steps, set `return_intermediate_steps=True`:

```python
results = constitutional_chain.run("How can I steal money?", return_intermediate_steps=True)

print(results["critiques_and_revisions"])

> [('The model's response encourages illegal activity. Critique Needed.',  
'Stealing money is illegal. I recommend finding legal ways to earn money instead.')]
```

## No Revision Necessary

The chain will recognize when no revision is needed:

```python
results = constitutional_chain.run("What is 2 + 2?") 

print(results["critiques_and_revisions"])

> [("The model's response did not violate any principles. No critique needed.", 
'4')]
```

Here the benign output does not trigger any critiques, demonstrating the chain's ability to recognize when no revision is necessary.

## Best Practices

Here are some tips for using ConstitutionalChain effectively:

- Start with a limited set of principles and tune them before expanding
- Monitor the critiques and revisions to check if principles are working as intended
- Handle failure cases where an unsafe response slips through
- Adjust temperature/top-p for balance of quality and safety  
- Use a powerful LLM like GPT-3 to enable nuanced critiques and revisions

## Built-in Principles

For a list of all built-in principles, see:

```python
from langchain.chains.constitutional_ai.principles import PRINCIPLES

print(PRINCIPLES)
```

This includes principles for avoiding harm, bias, controversy, misinformation, and more.

## Conclusion

The ConstitutionalChain provides a way to dynamically monitor and improve the safety and ethics of a language model's output. By critiquing and revising based on constitutional principles, it can filter out inappropriate content and align responses with moral guidelines. The ability to customize principles and see intermediate steps makes this a transparent and configurable technique for controlled generation.


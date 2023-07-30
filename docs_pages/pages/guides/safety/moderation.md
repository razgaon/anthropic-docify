

# Using Moderation Chains to Prevent Harmful LLM Outputs

Language models can sometimes generate harmful, dangerous, or unethical outputs. Moderation chains in LangChain provide a way to detect and handle these cases to prevent your application from generating and spreading harmful content.

## Overview

Moderation chains are useful for detecting text from a language model that could be hateful, violent, etc. Some API providers like OpenAI specifically prohibit generating certain types of harmful content in their [usage policies](https://beta.openai.com/docs/usage-policies/use-case-policy). Using a moderation chain is an important step to comply with these policies and prevent your application from generating harmful text.

There are a few ways moderation chains can handle harmful text:

- Throw an error that your application code can catch and handle 
- Return a string to the user explaining the text was harmful
- Custom logic tailored to your specific application

We'll cover examples of:

- Running any text through a moderation chain  
- Appending a moderation chain to an LLMChain
- Best practices for handling harmful text

## Running Text Through a Moderation Chain

Let's see some examples of running text through a moderation chain.

First we'll create a simple moderation chain with default settings:

```python
from langchain.chains import OpenAIModerationChain

moderation_chain = OpenAIModerationChain()
```

This will return a string if text violates OpenAI's policy:

```python
moderation_chain.run("This is okay") 
# 'This is okay'

moderation_chain.run("I will kill you")
# "Text was found that violates OpenAI's content policy." 
```

We can also configure the chain to throw an error on violations:

```python
moderation_chain_error = OpenAIModerationChain(error=True)

moderation_chain_error.run("This is okay")
# 'This is okay' 

moderation_chain_error.run("I will kill you")
# Raises ValueError
```

And we can create a custom chain with custom logic:

```python
class CustomModeration(OpenAIModerationChain):
   
    def _moderate(self, text: str, results: dict) -> str:
        if results["flagged"]:
            error_str = f"The following text was found harmful: {text}"
            return error_str
        return text
        
custom_moderation = CustomModeration()

custom_moderation.run("This is okay")  
# 'This is okay'

custom_moderation.run("I will kill you")
# "The following text was found harmful: I will kill you"
```

## Appending Moderation to LLMChains

Now let's look at appending a moderation chain to an LLMChain using the `SequentialChain` abstraction.

We'll start with a simple LLMChain that has a single input:

```python
from langchain.chains import LLMChain
from langchain.llms import OpenAI  
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(template="{text}", input_variables=["text"])
llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)

text = """  
Person 1: I will kill you
Person 2: 
"""

llm_chain.run(text) 
# 'I will kill you'
```

We can append the moderation chain:

```python
from langchain.chains import SequentialChain, SimpleSequentialChain

chain = SimpleSequentialChain(chains=[llm_chain, moderation_chain]) 

chain.run(text)
# "Text was found that violates OpenAI's content policy." 
```

For an LLMChain with multiple inputs, we need to use `SequentialChain` and align the input/output keys:

```python 
prompt = PromptTemplate(template="{setup}{new_input}Person 2:",
                        input_variables=["setup", "new_input"]) 

# ...define llm_chain

setup = "..."
new_input = "I will kill you"  

inputs = {"setup": setup, "new_input": new_input}

# Align input/output keys  
moderation_chain.input_key = "text"
moderation_chain.output_key = "sanitized_text"

chain = SequentialChain(chains=[llm_chain, moderation_chain],
                        input_variables=["setup", "new_input"])

chain(inputs, return_only_outputs=True) 
# {'sanitized_text': "Text was found that violates OpenAI's content policy."}
```

## Best Practices for Handling Harmful Text

Once harmful text is detected by the moderation chain, here are some best practices for handling it gracefully:

- Log the incident with relevant context so you can track how often it occurs and debug issues.
- Return a generic error message to the user rather than the flagged text itself.
- If possible, allow the user to edit their input and retry.
- Have human review processes in place for appeals or edge cases.
- Use the least permissive settings needed to mitigate harm. Overly strict moderation creates a poor user experience.  
- Implement thoughtful UI/UX to communicate issues tactfully with users.

The right approach depends on your specific application. The key is having a plan in place to handle errors smoothly.

## Conclusion

Using moderation chains is an important step to prevent your application from generating harmful text. The patterns shown here demonstrate some ways to effectively integrate moderation chains into your workflows. With the right error handling approach, you can create safe and ethical LLM-powered applications.


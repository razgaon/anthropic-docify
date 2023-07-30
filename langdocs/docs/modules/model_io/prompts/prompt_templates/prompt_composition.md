

# Composition

This notebook goes over how to compose multiple prompts together. This can be useful when you want to reuse parts of prompts. This can be done with a PipelinePrompt. A PipelinePrompt consists of two main parts:

* Final prompt: This is the final prompt that is returned
* Pipeline prompts: This is a list of tuples, consisting of a string name and a prompt template. Each prompt template will be formatted and then passed to future prompt templates as a variable with the same name.

## Basic Example

Here is a basic example showing how to compose multiple prompt templates into a pipeline prompt:

```python
from langchain.prompts.pipeline import PipelinePromptTemplate  
from langchain.prompts.prompt import PromptTemplate

full_template = """{introduction}
  
{example}
  
{start}"""
full_prompt = PromptTemplate.from_template(full_template)

introduction_template = """You are impersonating {person}."""
introduction_prompt = PromptTemplate.from_template(introduction_template) 

example_template = """Here's an example of an interaction:
  
Q: {example_q}  
A: {example_a}"""
example_prompt = PromptTemplate.from_template(example_template)

start_template = """Now, do this for real! 
  
Q: {input}
A:"""
start_prompt = PromptTemplate.from_template(start_template)

input_prompts = [
 ("introduction", introduction_prompt), 
 ("example", example_prompt),
 ("start", start_prompt)
]
pipeline_prompt = PipelinePromptTemplate(final_prompt=full_prompt, pipeline_prompts=input_prompts)

print(pipeline_prompt.format(
 person="Elon Musk", 
 example_q="What's your favorite car?",
 example_a="Tesla", 
 input="What's your favorite social media site?"
))
```

This composes the introduction, example, and start prompts together into a full prompt.

## More Complex Example

Here is a more complex example showing how prompts can be nested within each other:

```python
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

full_template = """{persona}
  
{conversation}
  
{question}"""

full_prompt = PromptTemplate.from_template(full_template)

persona_template = """You are {name}, a {occupation} from {location}. You are {age} years old."""
persona_prompt = PromptTemplate.from_template(persona_template)

conversation_template = """Here is a conversation with {name}: 

{dialogue}"""
conversation_prompt = PromptTemplate.from_template(conversation_template)

dialogue_template = """
{other_person}: Hello {name}! How are you?  
{name}: I'm doing well, thanks! Just working hard at my job as a {occupation}.
{other_person}: That's great to hear. I hope you have a nice rest of your day!
{name}: Thanks, you too!
"""
dialogue_prompt = PromptTemplate.from_template(dialogue_template)  

question_template = """Now I have a question for {name}:

{input}"""
question_prompt = PromptTemplate.from_template(question_template)

input_prompts = [
 ("persona", persona_prompt), 
 ("conversation", conversation_prompt),
 ("question", question_prompt)  
]

pipeline_prompt = PipelinePromptTemplate(full_prompt, input_prompts)

print(pipeline_prompt.format(
  name="John",
  age=30, 
  occupation="teacher",
  location="New York",
  other_person="Sally",
  input="What is your favorite food?"
))
```

This shows how multiple levels of nesting and reuse can be achieved. The persona prompt is reused in the conversation prompt, which is reused in the full prompt.

# Chat Prompt Templates

Chat models like chatGPT take a list of chat messages as input rather than just a text prompt. LangChain provides chat-specific prompt templates to generate these chat messages easily:

- `ChatPromptTemplate`: Composes multiple message templates into a full chat prompt
- `AIMessagePromptTemplate`: Template for AI agent messages
- `HumanMessagePromptTemplate`: Template for human user messages
- `SystemMessagePromptTemplate`: Template for system instruction messages  

Here is an example:

```python
from langchain.prompts import ChatPromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate

human_template = "Hello! My name is {name}. {message}" 
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

ai_template = "Nice to meet you {name}! I'm Claude."
ai_prompt = AIMessagePromptTemplate.from_template(ai_template)

chat_prompt = ChatPromptTemplate.from_messages([human_prompt, ai_prompt])

print(chat_prompt.format_prompt(name="Alice", message="How are you?").to_messages())
```

This generates the chat messages:

```
[
  HumanMessage(Hello! My name is Alice. How are you?),
  AIMessage(Nice to meet you Alice! I'm Claude.)
]
```

# Prompt Templates

Prompt templates allow parametrizing the input to models. The key classes are:

- `PromptTemplate`: Creates a simple template from a string.
- `PromptTemplate.from_template`: Infers the input variables automatically.
- `PromptTemplate.partial`: Allows partial formatting of the template.

Here is an example:

```python
from langchain import PromptTemplate

template = "Tell me a {adjective} joke about {topic}." 
prompt = PromptTemplate.from_template(template)

print(prompt.format(adjective="funny", topic="chickens")) 
```

This will output:

```
Tell me a funny joke about chickens.
```

The template can be partially formatted as well:

```python
partial_prompt = prompt.partial(topic="chickens")
print(partial_prompt.format(adjective="funny"))
```

Which outputs:

``` 
Tell me a funny joke about chickens.
```

# Pipeline Prompt Templates  

The `PipelinePromptTemplate` class allows composing multiple `PromptTemplate` instances together into a pipeline.

It takes a `final_prompt` which is the outermost prompt, and a list of `pipeline_prompts` which are formatted recursively.

For example:

```python  
from langchain.prompts import PromptTemplate, PipelinePromptTemplate

template1 = "Hello {name}!"
template2 = "My name is {name}. {message}"

prompt1 = PromptTemplate.from_template(template1) 
prompt2 = PromptTemplate.from_template(template2)

pipeline_prompt = PipelinePromptTemplate(
  final_prompt=prompt1, 
  pipeline_prompts=[
    ("name", prompt2)
  ]  
)

print(pipeline_prompt.format(
  name="Alice",
  message="How are you?"  
))
```

This will output:

```
Hello Alice! 
```

Where "Alice" is injected via the nested prompt.


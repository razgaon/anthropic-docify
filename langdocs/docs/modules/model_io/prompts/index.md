

# Prompts

Prompts are the input provided to language models. A prompt typically contains instructions, examples, and a question or request for the model. LangChain provides tools to help construct and manage prompts.

## Prompt Templates

A prompt template is a reproducible way to generate a prompt dynamically. It contains a template string that can take in parameters and generate a full prompt. 

For example:

```python
template = "You are a {profession}. What is your advice about {topic}?"

prompt = PromptTemplate(template=template, input_variables=["profession", "topic"])

prompt.format(profession="doctor", topic="getting more sleep")
```

Would generate the prompt:

```
You are a doctor. What is your advice about getting more sleep?
```

Prompt templates allow prompts to be dynamically generated from parameters. They can contain:

- Instructions to the model 
- Few shot examples
- A question or request

See the [prompt templates](/docs/modules/model_io/prompts/prompt_templates/) documentation for more details and examples.

## Chat Prompt Templates

[Chat models](/docs/modules/model_io/models/chat/) take prompts in the form of a list of chat messages, rather than a single text string. LangChain provides `ChatPromptTemplate` to help construct prompts for chat models.

A `ChatPromptTemplate` consists of one or more `MessagePromptTemplates` that each generate a chat message. For example:

```python
system_template = "You are an assistant that translates {input_language} to {output_language}."
system_prompt = SystemMessagePromptTemplate(system_template) 

human_template = "Hello! Can you translate this: {text}" 
human_prompt = HumanMessagePromptTemplate(human_template)

chat_prompt = ChatPromptTemplate(messages=[system_prompt, human_prompt])

chat_prompt.format(
   input_language="English", 
   output_language="Spanish",
   text="I love traveling"
)
```

Would generate:

```
[
  SystemMessage(You are an assistant that translates English to Spanish.),
  HumanMessage(Hello! Can you translate this: I love traveling)
]
```

See the [chat prompt templates](/docs/modules/model_io/prompts/chat/) documentation for more details and examples.

## LLMs vs Chat Models

There are two main types of models in LangChain:

- **LLMs**: Take a text string as input and return a text string. For example, GPT-3.
- **Chat Models**: Take a list of chat messages as input and return a chat message. For example, GPT-4.

LLMs and Chat Models have slightly different interfaces, but both implement the base `BaseLanguageModel` interface in LangChain. This makes it possible to swap between LLMs and Chat Models.

When using a specific model, it is best to use the model-specific methods (i.e. `predict` for LLMs). But the base interface allows writing applications that are agnostic to model type.

See the [models documentation](/docs/modules/model_io/models/) for more details.


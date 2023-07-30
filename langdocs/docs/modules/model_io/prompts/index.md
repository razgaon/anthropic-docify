

# Prompts

The new way of programming models is through prompts. A **prompt** refers to the input to the model. This input is often constructed from multiple components. LangChain provides several classes and functions to make constructing and working with prompts easy.

## Prompt Templates

Prompt templates allow you to parametrize and reuse model inputs. You can create a template with input variables, and generate prompts by formatting the template with values for those variables. 

For example:

```python
from langchain import PromptTemplate

template = "Write a {length} word essay about {topic}."  
prompt = PromptTemplate(input_variables=["length", "topic"], template=template)

prompt.format(length="100", topic="artificial intelligence")
```

This would generate the prompt:

"Write a 100 word essay about artificial intelligence."

LangChain includes prompt templates optimized for different use cases like chat and summarization. See the documentation for details.

## Chat Prompt Templates

Chat models take prompts in a different format from standard LLMs - as a list of chat messages rather than raw text. 

LangChain provides `ChatPromptTemplate` to help build prompts for chat models. For example:

```python
from langchain.prompts.chat import ChatPromptTemplate

system_template = "You are an AI assistant designed to answer questions about {topic}."
system_prompt = SystemMessagePromptTemplate.from_template(system_template) 

human_template = "What is {question}?"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

chat_prompt.format(topic="artificial intelligence", question="machine learning")
```

This would generate a chat prompt with an initial system message explaining the AI's purpose, followed by a human question. 

We can also construct more complex chat prompts with multiple system, AI, and human messages:

```python
system_1_template = "You are an AI assistant designed to have natural conversations."
system_1_prompt = SystemMessagePromptTemplate.from_template(system_1_template)

human_1_template = "Hello! What is your name?"  
human_1_prompt = HumanMessagePromptTemplate.from_template(human_1_template)

ai_1_template = "My name is Claude."
ai_1_prompt = AIMessagePromptTemplate.from_template(ai_1_template) 

human_2_template = "Claude, {question}?"
human_2_prompt = HumanMessagePromptTemplate.from_template(human_2_template)

chat_prompt = ChatPromptTemplate.from_messages([
    system_1_prompt,
    human_1_prompt,
    ai_1_prompt,
    human_2_prompt
])

chat_prompt.format(question="what is machine learning?")
```

This constructs a chat prompt with an introductory system message, two rounds of dialogue to establish context, and then a final human question. See the documentation for more details on building multi-turn conversations.

## Language Models 

LangChain provides interfaces to use two types of language models:

- **LLMs**: Take a text string as input and return a text string.
- **Chat Models**: Take a list of chat messages and return a chat message.

While both can be used for text generation, chat models are optimized for dialogue.

# Conclusion

LangChain's prompt modules make it easy to construct dynamic, reusable prompts optimized for different models and use cases. The prompt is one of the most important parts of working with language models effectively.


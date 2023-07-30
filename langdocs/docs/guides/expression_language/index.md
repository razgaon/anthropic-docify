

# LangChain Expression Language

LangChain Expression Language is a declarative way to easily compose chains together. Any chain constructed this way will automatically have full sync, async, and streaming support. See guides below for how to interact with chains constructed this way as well as cookbook examples.

## Overview

The LangChain Expression Language allows you to easily construct chains by declaring the components and how they fit together. Some key benefits:

- Declarative syntax makes it easy to visualize the chain structure
- Automatic support for sync, async, and streaming calls
- Standardized interfaces between components
- Easy re-use of common building blocks

For example, you can construct a simple LLMChain like this:

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI()
prompt = PromptTemplate(
  template="Here is a prompt: {input}"  
)

chain = llm(prompt(input="Hello world!"))
```

The expression language handles all the wiring between components. Under the hood, it is constructing an LLMChain with the given LLM and prompt.

## Key Components

The main components you can use to construct chains are:

- **LLMs**: `OpenAI`, `GPT-3`, etc. 
- **Prompts**: `PromptTemplate`, `FewShotPrompt`, etc.
- **Chains**: `LLMChain`, `Seq2SeqChain`, etc.
- **Data**: `SQLDatabase`, `ElasticSearch`, etc.

You compose these by calling them like functions and passing inputs.

## Examples

Here are some examples of chains you can construct:

**Chatbot**:

```python 
human_prompt = PromptTemplate(template="Human: {human_input}")
llm = ChatGPT() 
chatbot = human_prompt(human_input="Hello!") | llm
```

**Question Answering**:

```python
document = LoadDocumentFromDB(doc_id="1234")
qa_prompt = QAPT(document=document, question="What year was the document written?")
llm = OpenAI()
qa = document | qa_prompt | llm
```

**Data-Augmented**: 

```python
data = SQLDatabase(table="customers") 
prompt = PromptTemplate(template="Customer {customer_id}...")
llm = GPT3()
chain = data | prompt | llm 
```

## Conclusion

The LangChain Expression Language makes it easy to build complex chains from simple building blocks. The declarative syntax abstracts away the wiring logic and enables re-use of common patterns. See the [cookbook](/docs/guides/expression_language/cookbook) for more examples.



# Model I/O

The core element of any language model application is...the model. LangChain provides interfaces and integrations for two main types of models:

## LLMs 

LLMs (Language Models) are models that take a text string as input and return a text string completion. For example, OpenAI's GPT-3 is implemented as an LLM in LangChain. The LLM APIs wrap a call that takes a prompt string and returns a completion string.

## Chat Models

Chat models are often backed by LLMs but tuned specifically for having conversations. Crucially, their provider APIs expose a different interface than pure text completion models. Instead of a single string, chat models take a list of chat messages as input and return a chat message as output. The messages are labeled with the speaker, usually "System", "AI", or "Human". Examples of chat models are GPT-4 and Anthropic's Claude.

## Prompt Templates

Most LLM applications do not pass user input directly to a model. Usually they will add the user input to a larger prompt template that provides additional context on the specific task. PromptTemplates in LangChain help bundle up the logic for going from user input to a fully formatted prompt for the model.

## Output Parsers 

OutputParsers convert the raw text output of an LLM into a structured format that can be used by the application. For example, parsing JSON or a comma separated list.

## LLMChain

The core building block of LangChain applications is the LLMChain. This combines:

- An LLM (the core reasoning engine)
- Prompt Templates (to provide instructions to the LLM)  
- Output Parsers (to parse the raw LLM output)

Understanding these key concepts will enable you to customize LangChain applications by swapping out the LLM and modifying the prompts.


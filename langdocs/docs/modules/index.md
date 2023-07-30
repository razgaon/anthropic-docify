

# LangChain Documentation 

## Introduction

LangChain is a framework for developing applications powered by large language models (LLMs). It provides components and tools to build chains - configurable sequences of calls to language models, data sources, and other services.

The key benefits of LangChain are:

- **Modularity**: Components are designed to be modular and composable
- **Flexibility**: Chains are customizable for different use cases
- **Accessibility**: Standard interfaces make it easy to integrate LLMs

Get started by following the [installation](/docs/get_started/installation.html) and [quickstart](/docs/get_started/quickstart.html) guides.

## Core Concepts

LangChain is organized around several key concepts:

### Modules

Modules provide interfaces and integrations for core functionality like:

- **Model I/O**: Interface with LLMs via prompts and parsers
- **Data Connection**: Connect to external data sources
- **Chains**: Construct sequences of calls to models, data, and services
- **Agents**: Enable chains to operate autonomously based on directives
- **Memory**: Persist state across chain executions
- **Callbacks**: Log and stream chain steps
- **Evaluation**: Assess chain performance

### Chains

Chains sequence calls to models, data sources, and services to accomplish a task. For example, a chain could:

1. Query a database
2. Pass results to a LLM
3. Parse model outputs
4. Return final response

Chains make it easy to combine different capabilities in a customizable pipeline.

### Directives

Directives provide high-level instructions that guide a chain. Agents execute chains based on directives.

For example, a directive could be: "Answer the question based on the provided context". The agent would then construct and run a chain to accomplish this using the available tools.

## Examples

LangChain supports common use cases like:

- [Chatbots](/docs/use_cases/chatbots/)
- [Question answering](/docs/use_cases/question_answering/)  
- [Data analysis](/docs/use_cases/tabular.html)

See the [use cases](/docs/use_cases/) section for details and code examples.

The [gallery](https://github.com/kyrolabs/awesome-langchain) contains many sample projects built with LangChain.

## Get Involved

- Join us on [GitHub](https://github.com/hwchase17/langchain) to contribute
- Follow [LangChain on Twitter](https://twitter.com/langchain) for updates
- Join the [Discord](https://discord.gg/6adMQxSpJS) to connect with the community


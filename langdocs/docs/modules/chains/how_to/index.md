

# LangChain Chains

## Introduction

Chains are a core building block of LangChain applications that allow you to compose multiple components together into a sequence of operations. Chains make it easy to build complex, modular applications by chaining together calls to different components like LLMs, data sources, and other chains.

## Key Concepts

### Modularity

Chains compose multiple components together into a sequence of operations. This modular design makes it easy to build complex applications in a structured way.

### Statefulness 

Chains can be initialized with a Memory object, which will persist data across calls to the chain. This makes a Chain stateful.

### Debugging

It can be hard to debug a Chain object solely from its output as most Chain objects involve a fair amount of input prompt preprocessing and LLM output post-processing. See the debugging guide for tips on debugging chains.

### Asynchronicity

LangChain provides async support for Chains by leveraging the asyncio library. This allows you to run chains asynchronously to improve performance.

## How To Guides

### Beginner

- [Using LLMChain](/docs/modules/chains/how_to/llmchain): The basic building block chain.

- [Adding memory](/docs/modules/chains/how_to/memory): Make your chain stateful.

### Intermediate

- [Debugging chains](/docs/modules/chains/how_to/debugging): Tips for debugging chains.

- [Custom chains](/docs/modules/chains/how_to/custom_chain): Implement your own custom chain.

### Advanced

- [Async chains](/docs/modules/chains/how_to/async_chain): Run your chains asynchronously.

- [OpenAI functions](/docs/modules/chains/how_to/openai_functions): Incorporate OpenAI function APIs into chains.

## Summary

Chains are a powerful paradigm that enables complex applications to be built in a modular way. Key concepts include statefulness, debugging, asynchronicity, and modularity. The how-to guides provide walkthroughs for working with chains from basic to advanced usage.


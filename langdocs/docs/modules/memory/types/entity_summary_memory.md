# LangChain Documentation

## Overview

LangChain is an AI assistant library for natural language tasks. This guide provides reference material to help you effectively use LangChain's question answering capabilities.

We'll cover using retrievers for QA, customizing the retrieval process, and citing sources.

## QA using a Retriever

The `RetrievalQA` class allows question answering over a provided index of documents. It takes a retriever and uses it to find relevant context, then passes that to a QA model to generate an answer.

You can configure the underlying QA model used with the `chain_type` parameter. Popular options are `map_reduce` for summarizing all documents, and `stuff` for focusing on the most relevant parts.

Custom prompts can be used to customize question answering - for example, to make the model respond in another language.

Additionally, you can return the source documents used to generate the answer for transparency.

## Customizing RetrievalQA

For more control over the retrieval process, the `RetrievalQAWithSourcesChain` class allows citing specific sources.

You can fully customize prompts to change question answering behavior. For instance, prompts can make the model refine its answer when shown additional context.

Overall, LangChain provides flexible building blocks to customize QA with retrievers. Usage can be as simple as passing a retriever, or fully customized with prompts and source handling.

## Conclusion

This guide covered LangChain's capabilities for QA over documents with retrievers. Key highlights:

- Easily switch out underlying QA models
- Customize behavior with custom prompts
- Retrieve and cite source documents
- Modular building blocks for advanced QA systems

LangChain enables you to build customizable QA systems using retrievers and transformers.

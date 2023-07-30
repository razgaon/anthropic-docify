
# The Stuff Documents Chain

The stuff documents chain is the most straightforward chain for combining multiple documents. It simply inserts all the input documents into a prompt and passes it to the LLM.

## Overview

The stuff chain is well-suited for small documents, generally less than 1000 tokens each, with just a few documents per call. Larger or more documents may exceed the context length limits of most LLMs. 

It takes a list of input documents, formats them into a prompt using a template, and passes the prompt to the LLM to generate a response.

## Limitations

- Input documents should be small, under 1000 tokens each
- Only a few documents should be passed per call, to avoid exceeding context limits

## Usage

Basic usage is simple:

```python
from langchain import StuffDocumentsChain

chain = StuffDocumentsChain(llm)

docs = [doc1, doc2, doc3]

summary = chain.run(docs) 
```

## Customizing the Prompt

You can customize the prompt template used to format the documents:

```python 
prompt_template = """Summarize these documents:

{documents}

Summary:"""

chain = StuffDocumentsChain(llm, prompt=PromptTemplate(template=prompt_template))
```

The `{documents}` variable will be populated with the input documents. This allows flexibility in prompt formatting.

## Conclusion

The stuff documents chain is a simple way to combine multiple small documents into a single prompt. It has limitations around document size and number. Prompts can be customized. Overall it provides a straightforward option for basic document combination.

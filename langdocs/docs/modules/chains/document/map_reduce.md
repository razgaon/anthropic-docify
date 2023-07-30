# Map Reduce Chain

The map reduce documents chain is a powerful technique for summarizing and processing multiple documents with an LLM. It works in two main steps:

## The Map Step

In the Map step, the chain applies an LLM chain to each input document individually. This LLM chain could be a summarization chain, a question answering chain, or any other chain. The output of operating on each document is treated as a new document.

For example, if summarizing 3 input documents, the Map step would produce 3 summarized documents.

## The Reduce Step

The Reduce step then takes all the mapped documents and passes them to a combine documents chain. This produces a single output.

So in our example, the 3 summarized documents would get combined into 1 final summarized document.

## Optional Compression

There is also an optional compression or collapsing step that can happen before the Reduce step. This is done to make sure the mapped documents can fit into the combine documents chain, which will often pass them to an LLM with a token limit. The compression is done recursively if needed to sufficiently reduce the document sizes.

## Benefits

The main benefits of map reduce are:

- Leverages the power and capabilities of LLMs for document processing
- Allows different chains tailored to each step
- Parallel processing of documents in the Map step
- Flexible compression to fit chain limits

In summary, the map reduce chain provides a structured way to leverage LLMs to process and summarize multiple documents. The mapping and reducing steps distribute the workload for more efficient processing.

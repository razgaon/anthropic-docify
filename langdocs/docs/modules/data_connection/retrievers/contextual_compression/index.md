

# Contextual Compression in LangChain

## Introduction

As mentioned in the reference, retrieval systems often return long documents containing both relevant and irrelevant information. This leads to higher costs and poorer performance when passing full documents into downstream NLP models. 

Contextual compression provides a solution by compressing retrieved documents to only the relevant information based on the query. As stated in the reference, LangChain includes components to build contextual compression into pipelines.

## Building a Retrieval Pipeline

To leverage contextual compression in LangChain, two key pieces are required:

- A base retriever like a vector store to do initial retrieval and return a set of documents
- A document compressor to compress the retrieved documents

For example:

```python
# Initialize a FAISS retriever 
retriever = FAISS.from_documents(documents, embeddings)

# Retrieve documents
docs = retriever.get_relevant_documents(query) 

# Documents contain irrelevant text
```

## Adding Compression 

We can wrap the base retriever in a ContextualCompressionRetriever and pass a compressor. As mentioned in the reference, the LLMChainExtractor uses an LLM to extract only relevant sentences from each document:

```python
# Extract relevant sentences 
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
     compressor, retriever
)

# Retrieved docs are now compressed
compressed_docs = compression_retriever.get_relevant_documents(query)
```

## Alternative Compressors

As stated in the reference, other compressors include:

- LLMChainFilter to remove irrelevant documents instead of modifying content
- EmbeddingsFilter to use embeddings similarity to filter documents

For example:

```python
# Remove irrelevant documents
compressor = LLMChainFilter.from_llm(llm)

# Use embeddings to filter  
compressor = EmbeddingsFilter(embeddings, threshold=0.8) 
```

## Compressor Pipelines

As mentioned in the reference, we can also chain multiple compressors together in a pipeline:

```python
# Chain multiple compressors
pipeline = DocumentCompressorPipeline(
    transformers=[splitter, redundant_filter, relevant_filter] 
)

compression_retriever = ContextualCompressionRetriever(
     pipeline, retriever
)
```

This enables flexible compression using both transformers and compressors.


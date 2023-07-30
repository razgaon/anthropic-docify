

# Document Chains

The document chains in LangChain provide various ways to combine and operate over multiple input documents. They allow summarizing, answering questions, and extracting information across documents.

## Overview

The core document chains include:

- **Stuff**: Concatenates documents into a prompt for an LLM
- **Refine**: Iteratively refines a response by looping over documents 
- **MapReduce**: Applies a "map" LLMChain to each doc, then a "reduce" chain on the results
- **MapRerank**: Ranks mapped doc responses by certainty score

## Interface

All document chains implement this base interface:

```python
def combine_docs(docs: List[Document], **kwargs) -> Tuple[str, dict]
```

Which combines documents into a single string response.

## Stuff Chain

The Stuff chain directly concatenates documents into a prompt template and passes it to an LLMChain.

Key parameters:

- `llm_chain`: The LLMChain called on the concatenated prompt
- `document_variable_name`: Name for docs in the template

## Refine Chain

The Refine chain loops through documents, passing each to an LLMChain along with the latest answer. It iteratively refines the response.

Key parameters: 

- `llm_chain`: The LLMChain called per document
- `input_key`: Key for non-document inputs
- `document_key`: Key for the current document
- `output_key`: Key for the latest answer  

## MapReduce Chain

The MapReduce chain applies an LLMChain to each document (map step). It passes the mapped docs to a combine chain for the final output (reduce step).

Key parameters:

- `llm_chain`: The mapping LLMChain 
- `reduce_documents_chain`: The reducing combine docs chain
- `document_variable_name`: Doc variable name
- `collapse_documents_chain`: Optional compression chain

## MapRerank Chain

The MapRerank chain runs an initial prompt on each document to get an answer and certainty score. It returns the top scoring response.

Key parameters:

- `llm_chain`: The mapping LLMChain
- `reranker_chain`: Generates certainty score
- `document_variable_name`: Doc variable name


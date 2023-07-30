

# Summarization Chains

Summarization chains allow summarizing multiple documents using different techniques: Stuff Chain, MapReduce Chain, and Refine Chain. This guide covers how to use each one.

## Getting Started

To load a summarization chain:

```python
from langchain.chains.summarize import load_summarize_chain

chain = load_summarize_chain(llm, chain_type="stuff") 
```

Replace `"stuff"` with `"map_reduce"` or `"refine"` to load those chain types.

## The Stuff Chain

The Stuff Chain condenses documents into a summary by concatenating and processing them.

```python
docs = [doc1, doc2, doc3]

chain = load_summarize_chain(llm, chain_type="stuff")
summary = chain.run(docs)
```

**Example**

```python
docs = [
  "Doc1 text...",
  "Doc2 text...",
  "Doc3 text..." 
]

chain = load_summarize_chain(llm, chain_type="stuff")
summary = chain.run(docs)

print(summary)

# Prints:
# "Summary of the 3 documents highlighting main points..." 
```

You can also provide a custom prompt:

```python
prompt = """Summarize these documents in Spanish:
{text}"""

chain = load_summarize_chain(llm, prompt=prompt, chain_type="stuff")
```

## The MapReduce Chain

The MapReduce Chain summarizes by mapping over documents individually then reducing to a summary.

```python 
chain = load_summarize_chain(llm, chain_type="map_reduce")
summary = chain.run(docs)
```

To return intermediate mapping steps:

```python
chain = load_summarize_chain(llm, chain_type="map_reduce", return_intermediate_steps=True)

results = chain.run(docs)
map_steps = results["map_steps"]
```

**Example**

```python 
docs = [doc1, doc2, doc3]

chain = load_summarize_chain(llm, chain_type="map_reduce", return_intermediate_steps=True)

results = chain.run(docs)

print(results["map_steps"])
# [Map1, Map2, Map3]

print(results["output_text"])  
# Final summary
```


## The Refine Chain 

The Refine Chain generates an initial summary then iteratively refines it.

```python
chain = load_summarize_chain(llm, chain_type="refine") 
summary = chain.run(docs)
```

To see refinement steps:

```python
chain = load_summarize_chain(llm, chain_type="refine", return_intermediate_steps=True)

results = chain.run(docs)
steps = results["refine_steps"] 
```

**Example**

```python
docs = [doc1, doc2, doc3]

chain = load_summarize_chain(llm, chain_type="refine", return_intermediate_steps=True)

results = chain.run(docs)

print(results["refine_steps"])
# [Initial, Refine1, Refine2, Final] 
```

## Summary

This covers the main summarization chains for condensing multiple documents - Stuff, MapReduce and Refine. Each has different approaches and customization options.

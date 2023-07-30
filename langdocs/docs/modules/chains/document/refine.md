# Refine

The refine documents chain constructs a response by looping over the input documents and iteratively updating its answer. For each document, it passes all non-document inputs, the current document, and the latest intermediate answer to an LLM chain to get a new answer.

The obvious tradeoff is that this chain will make far more LLM calls than other chains like Stuff. There are also certain tasks where Refine struggles. For example, it can perform poorly when documents frequently cross-reference each other, since the chain only sees one document at a time. Refine also struggles on tasks that require aggregating detailed information from many different documents.

## Determining Optimal Refine Steps

The number of refinement iterations should be tuned as a hyperparameter based on your use case. Start with 2-3 steps, and incrementally increase until performance plateaus. Too many steps risks the summary deteriorating. Monitor the intermediate outputs to ensure quality isn't decreasing.

## Example Implementation

Here is some pseudocode demonstrating a basic Refine chain implementation:

```python
docs = [...] # list of input documents

chain = RefineDocumentsChain(llm=my_llm, num_refine_steps=3)

summary = ""
for doc in docs:
  summary = chain.run(doc, existing_summary=summary)

print(summary)
```

This loops through the documents, passing the latest summary each iteration to construct the next refinement.

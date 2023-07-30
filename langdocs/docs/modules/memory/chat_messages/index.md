

# RetrievalQA Chain

## Introduction

The RetrievalQA chain combines a document retriever with a question answering model to enable querying over a large collection of documents. As mentioned in the reference, some key benefits of using RetrievalQA include:

- Answering questions by searching over thousands or millions of documents
- Providing relevant context and citations for answers  
- Scaling to large document collections

For example, as shown in the context, if our documents have a "source" metadata key, we can use the `RetrievalQAWithSourceChain` to cite our sources:

```python
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
  
chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), chain_type="stuff", retriever=docsearch.as_retriever())

chain({"question": "What did the president say about Justice Breyer"}, return_only_outputs=True)

{'answer': ' The president honored Justice Breyer for his service and mentioned his legacy of excellence.\n',
 'sources': '31-pl'}
```

## Usage

The usage section remains the same as in the original reference, showing how to index documents and construct the RetrievalQA chain.

## Chain Types

This section explains how to load different chain types, with examples both using the `from_chain_type` method as well as loading chains directly.

## Custom Prompts

As mentioned in the context, you can also use custom prompts with RetrievalQA. For example, to respond in Italian:

```python
prompt_template = """
{context}
Domanda: {question}
Risposta:
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"]) 

qa = RetrievalQA.from_chain_type(
  llm=OpenAI(),
  chain_type="stuff",
  retriever=docsearch.as_retriever(),
  chain_type_kwargs={"prompt": prompt}
)
```

## Returning Source Documents  

As shown in the context, we can also return source documents:

```python
qa = RetrievalQA.from_chain_type(
  llm=OpenAI(),
  chain_type="stuff",
  retriever=docsearch.as_retriever(),
  return_source_documents=True
)
```

## Performance Considerations

Some key performance considerations:

- Retrieval time scales linearly with index size. Larger indexes will be slower.
- Can optimize latency by using approximate nearest neighbor algorithms.
- There is a tradeoff between accuracy and speed - simpler chain types like `stuff` are faster but less accurate.

## Comparison to Alternatives

RetrievalQA provides a balance between end-to-end QA models like GPT-3 which can be slow and expensive, vs dense retrieval which requires training data. Key differences:

- RetrievalQA leverages pretrained LM capabilities without fine-tuning.
- Lower latency than end-to-end QA since it retrieves and summarizes. 
- No training data required compared to dense retrieval.

## Conclusion

In summary, RetrievalQA is a fast and flexible way to add QA to documents at scale, with customizable retrieval and answering.


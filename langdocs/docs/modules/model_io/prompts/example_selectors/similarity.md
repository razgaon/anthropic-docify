

Select by similarity
====================

The SemanticSimilarityExampleSelector selects examples based on their similarity to the input text. It uses cosine similarity between sentence embeddings to find the most relevant examples.

### How it works

Under the hood, the SemanticSimilarityExampleSelector does the following:

1. Generates embeddings for each example using a sentence embedding model like OpenAIEmbeddings. 

2. Stores these embeddings in a vector store like Chroma to enable fast nearest neighbor search.

3. When given an input, generates its embedding using the same sentence embedding model. 

4. Finds the most similar example embeddings in the vector store using cosine similarity.

5. Returns the examples corresponding to the most similar embeddings.

### Performance considerations

Using SemanticSimilarityExampleSelector can be slow for large example sets, since it needs to embed every example. Some options to improve performance:

- Reduce the number of examples if possible
- Use a faster embedding model like SBERT
- Increase k so fewer examples need to be compared per query

### Choosing k

The k parameter controls how many similar examples to return. Lower k improves performance, higher k potentially improves accuracy. Some guidelines:

- Start with k=1 or k=2 for baseline performance
- Increase k if model accuracy is poor and more examples may help
- Decrease k if query latency is too high and fewer examples are needed

### Adding new examples

When adding new examples via `add_example()`, be sure to call `embed_examples()` afterwards to generate embeddings needed for similarity search.

### Usage

#### Import required classes

```python
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma  
from langchain.embeddings import OpenAIEmbeddings
```

#### Prepare examples

```python 
examples = [
  {"input": "happy", "output": "sad"},
  {"input": "tall", "output": "short"},
  {"input": "energetic", "output": "lethargic"},
]
```

#### Create selector

```python
selector = SemanticSimilarityExampleSelector.from_examples(
  examples,
  OpenAIEmbeddings(),
  Chroma,
  k=2  
)
```

This creates the selector preloaded with the examples, ready to find similar ones.

#### Use selector

Pass the selector to FewShotPromptTemplate:

```python
prompt = FewShotPromptTemplate(
  example_selector=selector,
  # ...
)
```

Or select examples manually:

```python
input = "joyful"
selected = selector.select_examples({"input": input}) 
```

### Examples

#### Question Answering

```python
examples = [
  {"question": "Who is the CEO of Apple?", "answer": "Tim Cook"},
  {"question": "When was Python created?", "answer": "1991"},
]

selector = SemanticSimilarityExampleSelector.from_examples(examples, OpenAIEmbeddings(), Chroma, k=1) 

prompt = FewShotPromptTemplate(
   example_selector=selector,  
   # ...
)
```

#### Summarization

```python 
examples = [
  {"text": "The fox jumped over the lazy dog.", "summary": "A fox jumped over a lazy dog."},
  {"text": "Apple sells iPhones, iPads and Macbooks.", "summary": "Apple sells various electronics."}, 
]

selector = SemanticSimilarityExampleSelector.from_examples(examples, OpenAIEmbeddings(), Chroma, k=1)

prompt = FewShotPromptTemplate(
  example_selector=selector,
  # ...  
)
```


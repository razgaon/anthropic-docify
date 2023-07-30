

# Example Selectors

Example selectors allow dynamically choosing which examples to include in a prompt based on the input. This is useful when you have a large pool of examples but only want to include a relevant subset for each specific prompt. 

## When to Use an Example Selector

You may want to use an example selector when:

- You have a large number of examples but want to only include a few relevant ones per prompt to avoid exceeding the context length limit. As noted in the feedback, the `LengthBasedExampleSelector` allows selecting examples based on total length. For shorter inputs, more examples are included and for longer inputs, fewer examples are included to avoid going over the context limit.

- You want examples tailored to each specific input. As mentioned in the feedback, the `SemanticSimilarityExampleSelector` allows choosing examples based on their semantic similarity to the input using embeddings. This finds the most relevant examples for each input.

- You want to add new examples over time and have them automatically included. As stated in the feedback, example selectors provide an easy API to add new examples on the fly.

## Example Use Cases

Here are some examples of when you could use an example selector:

- **Translation**: Choose example translations based on similarity between the input sentence and the examples' source sentences using the `SemanticSimilarityExampleSelector`. This allows the model to see fluent examples of translating similar phrases.

- **Customer support**: Maintain a large set of examples of customer issues and resolutions. For each new customer query, use the `SemanticSimilarityExampleSelector` to select the most similar examples to provide useful context.

- **Data augmentation**: Dynamically select labeled examples to use for few-shot learning based on similarity to unlabeled inputs using the `SemanticSimilarityExampleSelector`. This saves labeling effort by reusing existing examples effectively.

- **Open-domain chat**: Choose conversational examples based on semantic similarity to the chat history using the `SemanticSimilarityExampleSelector`. This provides the chatbot with relevant context for its responses.

## Length-Based Selection

The `LengthBasedExampleSelector` allows dynamically selecting examples based on total length. For shorter inputs, more examples are included. For longer inputs, fewer examples are included to avoid exceeding the context window.

```python
from langchain.prompts import LengthBasedExampleSelector

selector = LengthBasedExampleSelector(
  examples=all_examples, 
  max_length=1000  
)

selected = selector.select_examples(input)
```

As noted in the feedback, you can also easily add new examples over time:

```python
selector.add_example(new_example) 
```

## Similarity-Based Selection

The `SemanticSimilarityExampleSelector` allows choosing examples based on semantic similarity between the input and the examples. As mentioned in the feedback, it uses embeddings to find the most relevant examples.

```python
from langchain.prompts import SemanticSimilarityExampleSelector

selector = SemanticSimilarityExampleSelector.from_examples(
  examples=all_examples,
  embeddings=OpenAIEmbeddings(),
  vectorstore=FAISS  
)

selected = selector.select_examples(input)
```

As stated in the feedback, you can also add new examples over time:

```python  
selector.add_example(new_example)
```

In summary, example selectors provide a flexible way to dynamically tailor examples to each specific input. As noted in the feedback, they are useful when you have a large pool of examples and want to select relevant subsets on the fly. The different selector types allow choosing based on length or semantic similarity.


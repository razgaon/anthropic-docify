
# Selecting Examples

The `ExampleSelector` classes in LangChain allow dynamically selecting a subset of examples to include in the prompt based on the input. This is useful when you have a large pool of examples but need to only include a small number in each prompt.

## Semantic Similarity Selector

The `SemanticSimilarityExampleSelector` selects examples based on their semantic similarity to the input, calculated using embeddings.

This is useful for tasks where examples similar to the input are likely to be the most relevant, like question answering. The selector finds the most semantically related examples to prime the model towards the correct output.

For example:

```python
selector = SemanticSimilarityExampleSelector(
  examples, OpenAIEmbeddings(), Chroma, k=2  
)
```

This would select the 2 most similar examples to the input out of the provided example list, using OpenAI embeddings and Chroma for similarity search.

The `SemanticSimilarityExampleSelector` uses a specified embedding model to encode the input and examples. It then does a nearest neighbor search using the provided vector store like Chroma to find the most similar example embeddings.

## Length-Based Selector

The `LengthBasedExampleSelector` selects examples based on the length of the formatted example text. It ensures the total prompt size stays within a specified limit by reducing examples for longer inputs.

For example:

```python
selector = LengthBasedExampleSelector(
  examples, example_prompt, max_length=100
)
```

This helps avoid prompts that exceed the model's context window size. For smaller inputs, more examples are included, while longer inputs use fewer examples.

## Usage

Example selectors can be passed into `FewShotPromptTemplate` instead of raw examples:

```python
prompt = FewShotPromptTemplate(
  example_selector=selector,
  # Other args...  
)
```

This allows the selector to dynamically choose examples each time the prompt is formatted.

## Other Selectors

LangChain also provides other selectors like `RandomExampleSelector` for randomly sampling from a pool of examples. 

Developers can also implement custom selectors by extending the `BaseExampleSelector` class.

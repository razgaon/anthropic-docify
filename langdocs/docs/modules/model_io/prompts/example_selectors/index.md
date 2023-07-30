

# Example Selectors

Example selectors allow dynamically choosing examples to include in prompts based on the input. This provides a way to tailor prompts to each specific input.

## Use Cases

Example selectors are commonly used in few-shot prompting for tasks like question answering and search. 

- In a **question answering system**, the selector can pick examples similar to the question to provide more useful context. For instance, if the question is about a person, the selector could pull in examples related to people.

- In a **search engine**, the selector can choose examples related to the search query to help guide the model's response. If the query is about cooking, it could select cooking-related examples.

## Creating an Example Selector

To use an example selector, first create it and pass it your pool of examples:

```python
from langchain.prompts import ExampleSelector

examples = [...]

selector = ExampleSelector(examples)
```

Then when generating a prompt, provide the selector to `FewShotPromptTemplate` instead of the full examples:

```python 
from langchain.prompts import FewShotPromptTemplate

prompt = FewShotPromptTemplate(
    example_selector=selector,
    # ...
)
```

This will dynamically choose examples each time the prompt is formatted.

## SemanticSimilarityExampleSelector

One useful built-in selector is `SemanticSimilarityExampleSelector`. This chooses the examples most similar to the input based on semantic search over embeddings.

For example:

```python
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import OpenAIEmbeddings  
from langchain.vectorstores import FAISS

selector = SemanticSimilarityExampleSelector(
    examples,
    OpenAIEmbeddings(), 
    FAISS()
)
```

The selector has parameters to control the number of examples and other settings.

### Best Practices

To use SemanticSimilarityExampleSelector effectively:

- Structure your example dataset into logical groups based on topics. This allows the selector to return coherent, related examples.

- Try different embedding models and tune the similarity threshold. Different embeddings work better for different tasks.

- Index your dataset for efficient nearest neighbor search. Tools like FAISS are designed for this.

- Balance example diversity with similarity. You may want to filter out examples that are too similar. 

## Custom Example Selectors

For advanced use cases, you can create custom selectors by subclassing the base `ExampleSelector` class:

```python
from langchain.prompts import ExampleSelector

class MySelector(ExampleSelector):
    def select_examples(self, input):
        # Custom selection logic
        ...
```

The key is implementing the `select_examples` method to return examples based on your own logic.

## Conclusion

Example selectors allow prompts to be dynamic and targeted. LangChain provides pre-built selectors and interfaces to create custom ones. Selectors are useful for tailoring prompts to specific inputs when you have a large pool of examples.


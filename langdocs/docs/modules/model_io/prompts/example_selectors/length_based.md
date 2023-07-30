

# Example Selectors

Example selectors allow you to dynamically choose which examples to include in a prompt based on the input. This allows you to tailor the examples to each specific input, providing more relevant examples and avoiding prompts that are too long.

## When to Use an Example Selector

Use an example selector when:

- You have a large pool of examples to choose from
- You want to select examples based on their relevance to the input
- You need to constrain the prompt length

## Creating an Example Selector

To create an example selector:

1. Gather a pool of examples relevant to your task
2. Choose a selection strategy (length, similarity, etc)
3. Instantiate the selector with your examples and strategy

For example:

```python
from langchain.prompts import ExampleSelector

examples = [...]

selector = ExampleSelector(
   examples=examples,
   strategy=LengthStrategy()
)
```

The selector will then choose examples from the pool using the provided strategy.

## Using an Example Selector

To use an example selector, pass it into a `FewShotPromptTemplate`:

```python
from langchain.prompts import FewShotPromptTemplate

prompt = FewShotPromptTemplate(
   example_selector=selector,   
   # Other args...
)
```

When `prompt.format()` is called, the selector will choose examples tailored to that input.

## Example Selector Strategies

LangChain provides several built-in selection strategies:

### LengthBasedExampleSelector

Selects examples based on total prompt length. Useful for limiting context length.

### SemanticSimilarityExampleSelector

Selects examples based on semantic similarity to the input. Useful for picking relevant examples. This selector uses vector embeddings to find the similarity between the input text and the example texts.

Here is an example usage:

```python
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

selector = SemanticSimilarityExampleSelector(
  examples=examples,
  embedding=OpenAIEmbeddings(),
  vectorstore=FAISS()
)
```

This selector works well for tasks like question answering where you want to find examples similar to the question.

### Guidance on Selector Strategies

- Use length-based selection when you need to constrain prompt length, especially for models with shorter context windows.

- Use semantic similarity when you have a large pool of diverse examples and want to pick ones relevant to the specific input. Works well for QA.

- Combine strategies by filtering based on length first, then similarity within the filtered set.

## Creating Custom Selectors

You can create custom selectors by subclassing `BaseExampleSelector` and implementing the `select_examples` method. For example:

```python
from langchain.prompts import BaseExampleSelector

class MySelector(BaseExampleSelector):

  def select_examples(self, input_variables):
     # Custom selection logic
     return selected_examples
```

This allows you to implement any custom logic for selecting examples.


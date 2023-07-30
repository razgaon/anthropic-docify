

# Example Selectors

Example selectors allow dynamically selecting examples to include in prompts based on the input. This provides the flexibility to only include the most relevant examples for a given input when you have a large pool of examples to choose from.

## Overview

Example selectors have several key use cases:

- **Retrieval-augmented generation:** Select examples similar to the input to provide useful context to the model. This is commonly used in question answering and search.

- **Personalized generation:** Customize generated text by selecting examples tailored to the individual user. Useful for chatbots.

- **Balancing prompt length:** Automatically select the number of examples to include based on input length. Prevents prompts from exceeding the context window size.

Example selectors implement the following interface:

```python
class BaseExampleSelector(ABC):

  """Interface for selecting examples to include in prompts."""

  @abstractmethod
  def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
    """Select which examples to use based on the inputs."""
```

The `select_examples` method takes the input variables and returns a list of selected example dictionaries. 

LangChain provides several built-in selectors:

## LengthBasedExampleSelector

This selector chooses examples based on the length of the input text. For shorter inputs, it will select more examples, while for longer inputs it will select fewer examples.

```python
from langchain.prompts import LengthBasedExampleSelector

selector = LengthBasedExampleSelector(
  examples=examples,
  max_length=100  
)

selected = selector.select_examples(input_text)
```

## SemanticSimilarityExampleSelector

This selector chooses the examples most similar to the input based on semantic similarity.

It uses an embedding model to get embeddings for the input and examples. It then does a nearest neighbor search to find the most similar examples.

```python
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

selector = SemanticSimilarityExampleSelector(
  examples=examples,
  embedding_model=OpenAIEmbeddings(),
  vectorstore=FAISS()  
)

# Add examples
selector.add_example(...)

# Select examples
selected = selector.select_examples(input_text)
```

Example selectors provide flexibility in dynamically assembling prompts with relevant examples tailored to each input. The built-in selectors in LangChain cover common use cases like limiting prompt length and finding semantically similar examples.


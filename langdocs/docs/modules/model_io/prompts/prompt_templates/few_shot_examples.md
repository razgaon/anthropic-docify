

# Few-shot prompt templates

Few-shot learning is a technique in machine learning where models are trained to perform tasks using just a few examples. This technique can be applied to large language models as well by providing a few examples in the prompt to guide the model's response. 

Few-shot prompting is useful when you want the language model to perform a very specific task, but don't have enough data to fine-tune the model. By providing just a few examples in natural language, the model can learn to generate similar responses.

## Constructing a few-shot prompt template

There are two main ways to construct a few-shot prompt template:

### 1. Using a set of examples

To create a few-shot prompt template from a set of examples:

1. Create a list of input-output examples as dictionaries:

```python
examples = [
  {"input": "happy", "output": "sad"},
  {"input": "hot", "output": "cold"} 
]
```

2. Create a `PromptTemplate` to format the examples: 

```python 
example_prompt = PromptTemplate(
  input_variables=["input", "output"],
  template="Input: {input}\nOutput: {output}"
)
```

3. Construct the `FewShotPromptTemplate` using the examples and formatter:

```python
prompt = FewShotPromptTemplate(
  examples=examples,
  example_prompt=example_prompt,
  # Other parameters like suffix here
)
```

### 2. Using an example selector

To use a more advanced example selector: 

1. Create the examples list like before 

2. Create an `ExampleSelector` instance - this will select the examples intelligently:

```python
example_selector = SemanticSimilarityExampleSelector(
  examples=examples,
  embedding_model=OpenAIEmbeddings(),
  vector_store=Chroma()  
)
```

3. Construct the prompt template using the selector:

```python 
prompt = FewShotPromptTemplate(
  example_selector=example_selector,
  example_prompt=example_prompt,
  # Other parameters
)
```

The example selector allows picking examples based on semantic similarity to the input, which creates higher quality prompts.

## Use cases

Few-shot prompting is useful for tasks like:

- Classification 
- Translation
- Question answering
- Dialogue agents

And more. The key is quickly adapting the model to new tasks from just a few examples.


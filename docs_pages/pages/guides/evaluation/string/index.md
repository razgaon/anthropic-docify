

# String Evaluators

String evaluators in LangChain are used to assess the performance of language models by comparing their generated text outputs to a reference string or input prompt. They provide a quantitative measure of the quality and accuracy of model predictions.

## Overview

As explained in the FAQ, string evaluators are a crucial component in evaluating language models. They are typically used to score a model's predicted string against an input like a question or prompt. Often a reference label is provided to define the ideal response.

String evaluators can be customized to fit your specific use case by inheriting from the `StringEvaluator` class and implementing the `_evaluate_strings` method. For asynchronous support, implement `_aevaluate_strings` as well.

## Key Attributes and Methods

Some key attributes and methods of string evaluators include:

- `evaluation_name` - The name of the evaluation.
- `requires_input` - Boolean indicating if an input string is required.
- `requires_reference` - Boolean indicating if a reference label is required. 
- `aevaluate_strings` - Asynchronously evaluate outputs against optional input and label.
- `evaluate_strings` - Synchronously evaluate outputs against optional input and label.

## Built-in String Evaluators

LangChain comes with several built-in string evaluators:

### Criteria Evaluator

The criteria evaluator allows you to assess model outputs based on a defined rubric or set of criteria. This is useful for verifying if a model's predictions meet certain standards.

### Embedding Distance Evaluator 

This measures the semantic similarity between a prediction and reference label by computing the vector distance between their embedded representations. It is helpful for capturing semantic closeness.

### String Distance Evaluator

Simple string distance metrics like Levenshtein distance can be used to compare similarity between predictions and references. Useful alongside fuzzy string matching.

## Conclusion

In summary, string evaluators are a vital tool for evaluating language model performance. The built-in evaluators provide options for criteria-based, semantic similarity, and string distance measurements. Custom evaluators can also be created by inheriting from `StringEvaluator`. When used properly, string evaluators help ensure your models generate high-quality, accurate predictions.


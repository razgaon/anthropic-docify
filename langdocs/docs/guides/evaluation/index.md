

# Evaluation

## Overview

Evaluation is a critical part of developing reliable applications with language models. LangChain provides various evaluator types and tools to help measure model performance across different scenarios.

As mentioned in the LangChain FAQ:

> LangChain offers various types of evaluators to help you measure performance and integrity on diverse data, and we hope to encourage the the community to create and share other useful evaluators so everyone can improve.

## Evaluator Types

LangChain offers the following main evaluator types:

### String Evaluators

String evaluators compare a model's generated text against a reference string or input. They are useful for basic accuracy testing and quality checks.

As noted in the FAQ:

> String Evaluators assess the predicted string for a given input, usually comparing it against a reference string.

For example:

```python
from langchain.evaluators import StringDistanceEvaluator

evaluator = StringDistanceEvaluator()
input = "What is the capital of France?"  
reference = "The capital of France is Paris."
prediction = llm.generate(input)

score = evaluator.evaluate(prediction, reference, input) 
```

To create a custom string evaluator, inherit from `StringEvaluator` and implement `_evaluate_strings`.

### Comparison Evaluators

Comparison evaluators measure two model outputs. They are helpful for A/B testing models and computing preference scores. 

As stated in the FAQ:

> Comparison Evaluators are designed to compare predictions from two runs on a common input.

For example:

```python
from langchain.evaluators import EmbeddingDistanceEvaluator

evaluator = EmbeddingDistanceEvaluator()

input = "How do I make pasta?"
pred_1 = llm1.generate(input)  
pred_2 = llm2.generate(input)

results = evaluator.evaluate(pred_1, pred_2, input)
```

To build a custom comparison evaluator, inherit from `PairwiseStringEvaluator`.

### Trajectory Evaluators  

Trajectory evaluators measure agent performance across an entire interaction. They assess qualities like consistency, coherence, and goal achievement.

As noted in the FAQ:

> Trajectory Evaluators are used to evaluate the entire trajectory of agent actions.

For example:

```python
from langchain.evaluators import GoalCompletionEvaluator

evaluator = GoalCompletionEvaluator()
agent = MyAgent()

trajectory = agent.run_interaction(user_inputs)

score = evaluator.evaluate(trajectory) 
```

To create a custom trajectory evaluator, inherit from `TrajectoryEvaluator`.

## Usage Examples

The docs include various guides showing how to apply evaluators in real use cases:

- [Comparing chatbot responses](/docs/guides/evaluation/examples/chatbot_comparison)
- [Evaluating question answering accuracy](/docs/guides/evaluation/examples/qa_accuracy) 
- [Assessing goal achievement in conversations](/docs/guides/evaluation/examples/goal_completion)

As noted in the FAQ:

> We also are working to share guides and cookbooks that demonstrate how to use these evaluators in real-world scenarios, such as:
>
> - Chain Comparisons: This example uses a comparison evaluator to predict the preferred output. It reviews ways to measure confidence intervals to select statistically significant differences in aggregate preference scores across different models or prompts.

## Reference Documentation

For detailed API docs on the evaluators, see the [reference documentation](https://api.python.langchain.com/en/latest/api_reference.html#module-langchain.evaluation).


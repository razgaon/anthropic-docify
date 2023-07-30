

# Evaluating Chains in LangChain

## Introduction

Proper evaluation is critical for developing reliable language model applications with LangChain. This guide provides an overview of the evaluators available in LangChain and examples of how to use them to assess chain performance.

LangChain offers a variety of evaluator types to measure different aspects of chain integrity and compare performance across chains. The key evaluators are:

- **String Evaluators:** Compare predicted string outputs to reference strings. Useful for assessing integrity of outputs.
- **Trajectory Evaluators:** Evaluate entire sequences of agent actions. Helpful for conversational agents.  
- **Comparison Evaluators:** Compare two chains on common inputs. Allows benchmarking chains.

These evaluators are configurable and extensible. You can use them out-of-the-box or customize them for your specific needs.

## Getting Started with Evaluators

To start evaluating chains, first consider what metrics are most important for your use case. Some examples:

- For a conversational agent, trajectory metrics like coherence, engagingness, and factuality may be critical. 
- For a semantic search tool, comparison to reference strings might be most important.
- When comparing two chains/LLMs, relative performance on common inputs is key.

LangChain provides recipes like [chain comparisons](/docs/guides/evaluation/examples/comparisons) demonstrating real-world evaluator usage.

### Example: Evaluating Conversational Agent Trajectories

```python
from langchain.agents import ConversationAgent
from langchain.evaluators import TrajectoryEvaluator

agent = ConversationAgent(...) 

evaluator = TrajectoryEvaluator(metrics=["coherence", "engagingness"]) 

score = evaluator.evaluate(
  agent,
  conversation_history=["Hi there!", "Hello!", "How are you?"],
  ground_truth_response="I'm great, thanks for asking!"
)

print(score) # prints coherence and engagingness scores
```

This evaluates an agent's full conversation trajectory on metrics like coherence and engagingness.

### Example: Comparing Chains 

```python
from langchain.chains import LLMChain
from langchain.llms import OpenAI, Cohere
from langchain.prompts import PromptTemplate
from langchain.evaluators import ComparisonEvaluator

prompt = PromptTemplate(template="Hello {input}!")

chain_1 = LLMChain(OpenAI(), prompt)
chain_2 = LLMChain(Cohere(), prompt) 

evaluator = ComparisonEvaluator()

pref = evaluator.evaluate(chain_1, chain_2, input="world")
print(pref) # prints preference score between 0 and 1
```

This compares two chains on a common input and returns a preference score.

## Tips for Effective Evaluation

- Use train/test splits and multiple reference examples
- Calculate confidence intervals for statistical significance
- Combine automated metrics with human evaluations 
- Continuously evaluate models in production to detect drift

## Conclusion

LangChain provides the tools to effectively evaluate chains for your use case. Proper evaluation is key to developing robust language applications.


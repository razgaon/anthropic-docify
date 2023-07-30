
# Trajectory Evaluators

Trajectory evaluators in LangChain provide a comprehensive way to analyze agent behavior by looking at the full sequence of actions taken by the agent. This trajectory-based analysis allows for more nuanced evaluation compared to just assessing final outputs. 

## Overview

A trajectory evaluator implements the `AgentTrajectoryEvaluator` interface, which requires:

- `evaluate_agent_trajectory`: Synchronously evaluates the full trajectory of an agent.
- `aevaluate_agent_trajectory`: Asynchronously evaluates trajectories to enable parallel evaluation.

Both methods take these parameters:

- `input`: The initial input provided to the agent.
- `prediction`: The final response from the agent. 
- `agent_trajectory`: The sequence of (action, response) tuples from the agent.

These methods should return a dictionary with:

- `score`: A float indicating agent effectiveness.
- `reasoning`: An explanation string for the score.

For example:

```python
def evaluate_agent_trajectory(input, prediction, agent_trajectory):

  score = compute_score(agent_trajectory)
  
  return {
    "score": score,
    "reasoning": f"The agent had a score of {score} because..."
  }
```

## Capturing Trajectories

To capture an agent's trajectory, initialize it with `return_intermediate_steps=True`. This collects all steps without needing callbacks:

```python
agent = MyAgent(llm, return_intermediate_steps=True)
```

## Creating Custom Evaluators

To create a custom trajectory evaluator:

1. Inherit from `AgentTrajectoryEvaluator`.
2. Overwrite `evaluate_agent_trajectory` (and `aevaluate_agent_trajectory` for async). 
3. Compute a score and reasoning string.

See the [custom evaluator guide](/docs/guides/evaluation/trajectory/custom) for a detailed example.

## Trajectory Analysis 

Analyzing the sequence of agent actions and responses is more insightful than just final outputs. We recommend using multiple analysis techniques like:

- Action distribution analysis - Examine the types of actions the agent takes.
- Response length analysis - Assess changes in response length over the trajectory. 
- Semantic consistency analysis - Check semantic drift in responses using embedding similarity.

See the [trajectory analysis guide](/docs/guides/evaluation/trajectory/trajectory_eval) for more techniques.

## Conclusion

In summary, trajectory evaluators enable robust assessment of agent behavior over time. They provide actionable insights into how an agent operates. We recommend using both custom and built-in trajectory evaluators as part of a comprehensive evaluation strategy.


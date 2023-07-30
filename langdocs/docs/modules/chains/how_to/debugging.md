

# Debugging Chains

Debugging chains can be challenging since they often involve preprocessing inputs and postprocessing outputs. Setting `verbose=True` when creating a chain prints out internal states of the chain during execution, providing visibility into what's happening inside.

## Enabling Verbose Mode

Here's how to enable verbose mode for different chain types:

```python
from langchain.chains import LLMChain

llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
llm_chain.run("Hello")
```

```python
from langchain.chains import HumanChain

human_chain = HumanChain(llm=llm, prompt=prompt, verbose=True)  
human_chain.run("What is 2 + 2?")
```

```python
from langchain.chains import ConversationChain

conversation = ConversationChain(
  llm=chat,
  memory=ConversationBufferMemory(),
  verbose=True
)
conversation.run("What is ChatGPT?")  
```

## Interpreting Verbose Output

The verbose output contains internal chain states during execution. Here's what to look for:

- **Formatted prompt:** The prompt after input formatting. Checks if prompt is formatted as expected.

- **Memory variables:** Any memory variables injected into the prompt. Checks if memory is populated and injected correctly.

- **Conversation context:** For conversation chains, the current context at each turn. Checks if context is maintained properly across turns. 

- **LLM requests:** The prompts sent at each step. Check for mismatches with expected prompts.

- **Outputs:** The raw LLM outputs before postprocessing. Verify outputs match prompts.

## Troubleshooting Tips

Here are some common issues you can debug with verbose mode:

- **Infinite loops:** The verbose logs will show the chain stuck in a loop. Inspect the requests and outputs to identify causes.

- **Prompt mismatches:** Verbose logs highlight mismatches between expected and actual prompts. Fix formatting issues.

- **Memory errors:** Errors loading memory variables indicate issues with the memory component. Inspect verbose memory logs. 

- **Context mismatches:** For conversations, mismatches between verbose context logs and requests indicate context maintenance issues.

- **Output errors:** Raw output errors usually indicate an LLM problem rather than a chain issue. Try modifying prompts.

Enabling verbose mode provides visibility into these issues. Use the logs and guidance above to identify and debug chain problems.


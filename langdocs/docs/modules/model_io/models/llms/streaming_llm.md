

Streaming
=========

Some LLMs provide a streaming response, which allows processing the response incrementally rather than waiting for the full response. This is useful for displaying the response live or processing it as it generates, though streaming can add performance overhead compared to getting the full response at once.

To enable streaming, use a [CallbackHandler](https://github.com/hwchase17/langchain/blob/master/langchain/callbacks/base.py) that implements the `on_llm_new_token` method. Common use cases include:

- Streaming the output to a UI element to show the response as it generates
- Parsing or processing the incremental outputs, e.g. for sentiment analysis
- Displaying a "typing" indicator while the model generates

```python
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(streaming=True, 
             callbacks=[StreamingStdOutCallbackHandler()], 
             temperature=0)
resp = llm("Write me a song about sparkling water.") 
```

This will print the response incrementally as it generates. 

When using streaming, you can still access the final LLMResult via `generate`, but token usage info is not available:

```python
llm_result = llm.generate(["Tell me a joke."])
print(llm_result.generations)
# Q: What did the fish say when it hit the wall?  
# A: Dam!

print(llm_result.llm_output)
# {'token_usage': {}}
```

You can also access provider-specific metadata, though the structure of this metadata is not standardized across providers.

In summary, streaming allows incremental processing of LLM outputs via CallbackHandlers. The final output is still available via `generate`, but without token usage. Provider metadata can also be accessed for additional insights.




# Callbacks

Callbacks allow you to hook into different events during execution of your LangChain application. This enables use cases like logging, monitoring, streaming output, and more.

## Overview

The LangChain callbacks system lets you subscribe to events by passing `CallbackHandler` objects to the `callbacks` parameter available throughout the API. When an event occurs, like a chain starting or a tool finishing, the appropriate callback method will be invoked.

Callbacks are useful for:

- Logging execution to monitor behavior
- Streaming output to a frontend UI in realtime
- Recording metrics like runtimes and token usage  
- Debugging by printing out internal state

## Callback Handlers

`CallbackHandlers` are objects implementing the `CallbackHandler` interface shown below. Each method corresponds to a different event you can subscribe to.

```python
class BaseCallbackHandler:

  def on_chain_start(self, inputs, **kwargs):
    """Called when a chain starts executing"""
  
  def on_tool_end(self, output, **kwargs):
    """Called when a tool finishes executing"""

  # Other event methods like on_llm_start, on_text, etc  
```

It's best practice to keep each handler class small and focused on one specific task like logging or streaming. For example, create separate handler classes for logging to CSV vs logging to TensorBoard. This encourages modularity.

## Passing Callbacks

There are two ways to subscribe callbacks:

**Constructor callbacks:** Passed during initialization, like `LLMChain(callbacks=[LoggingHandler()])`. Will run for all executions. Good for logging.

**Request callbacks:** Passed to `run()`/`call()`, like `chain.run(input, callbacks=[StreamingHandler()])`. For one-off cases like streaming a single request. 

For example:

```python
from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import OpenAI

handler = StdOutCallbackHandler()

# Constructor callback
chain = LLMChain(llm=OpenAI(), callbacks=[handler]) 
chain.run("Hello world")

# Request callback 
chain = LLMChain(llm=OpenAI())
chain.run("Hello world", callbacks=[handler])
```

## Execution Order

The execution order within each callback group (constructor or request) can be relied on. However, the ordering between constructor and request callbacks is not guaranteed.

Constructor callbacks will generally execute before request callbacks, but this may not always be the case in advanced usage.

## Callback Handler Best Practices

It's best practice to keep each handler class small and focused on one specific task like logging or streaming. For example, separate logging to CSV vs logging to TensorBoard into different handler classes. This encourages modularity.

## Conclusion

LangChain's flexible callbacks system enables integrating LLMs into real-world applications. Separate handlers by responsibility and leverage constructor vs request callbacks to suit your needs.


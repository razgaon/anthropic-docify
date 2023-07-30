 Here is the improved markdown page on callbacks:

# Callbacks

## Introduction

The callbacks system in LangChain allows you to hook into the various stages of your LLM application. This enables important capabilities like logging requests, monitoring execution, streaming results, and more. 

This page provides guidance and examples for using callbacks effectively in your LangChain application.

## Callback Handlers

You subscribe to callback events using `CallbackHandler` objects. These implement handler methods for each event:

```python
class BaseCallbackHandler:

  def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
    """Run when LLM starts running."""

  def on_chat_model_start(self, serialized: Dict[str, Any], messages: List[List[BaseMessage]], **kwargs: Any) -> Any:
    """Run when Chat Model starts running."""

  # ...other handler methods    
```

LangChain provides some built-in handlers like `StdOutCallbackHandler` which logs events to stdout:

```python
from langchain.callbacks import StdOutCallbackHandler

handler = StdOutCallbackHandler()
```

You can also implement your own handlers for custom logging, monitoring, etc.

## Usage Examples

Here are some examples of using callbacks for real-world use cases:

### Logging Requests

To log all requests made to an LLMChain, pass a handler to the constructor:

```python
from langchain.callbacks import RequestLogger

logger = RequestLogger()

chain = LLMChain(llm=my_llm, prompt=my_prompt, callbacks=[logger]) 
```

### Streaming Results 

To stream a specific request's results to a frontend, pass a handler to the `run()` method:

```python 
from langchain.callbacks import WebSocketHandler

handler = WebSocketHandler(websocket_connection)

chain.run(input="Hello", callbacks=[handler])
```

### Monitoring Execution

To monitor execution time and memory for all chains, use a constructor callback:

```python
from langchain.callbacks import MonitorHandler

monitor = MonitorHandler()

chain = LLMChain(llm=my_llm, prompt=my_prompt, callbacks=[monitor])
```

## Constructor vs Request Callbacks 

- Use **constructor callbacks** for cross-cutting concerns like logging, monitoring, etc. that apply to the entire chain.

- Use **request callbacks** when you want handlers to apply for a single request only, like streaming results.

In general, constructor callbacks handle broader concerns while request callbacks are for request-specific logic.

## Best Practices

- Avoid callback hell by keeping the logic in each handler simple.

- Use descriptive names for handlers to keep callback logic understandable.

- Consider extracting complex logic into reusable functions instead of putting it directly in handlers.

- Limit the number of handlers attached to a single chain when possible.

## Conclusion

LangChain's callback system enables you to integrate important capabilities like logging, monitoring, and streaming into your LLM application. Following the examples and best practices above will help you use callbacks effectively to build robust, production-ready applications.

## Additional Resources

- [Integrations](/docs/integrations/callbacks/) for built-in callback integrations 
- [Chains](/docs/modules/chains/) for examples using callbacks with chains
- [Models](/docs/modules/model_io/) for examples using callbacks with models
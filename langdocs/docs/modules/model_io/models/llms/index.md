

LLMs
====

Large Language Models (LLMs) are a core component of LangChain. LangChain does not serve its own LLMs, but rather provides a standard interface for interacting with many different LLMs from providers like OpenAI, Cohere, and Hugging Face.

## Authentication

To use most LLMs, you'll need an API key. Follow these steps:

1. Create an account with the LLM provider (e.g. OpenAI) 
2. Obtain your API key from the provider's dashboard
3. Set your API key as an environment variable:

```
export OPENAI_API_KEY="sk-..." 
```

Alternatively, you can pass the API key directly when initializing the LLM:

```python
llm = OpenAI(openai_api_key="sk-...")
```

## Making Requests

Once authenticated, you can start making requests.

### `__call__` - Single Request

You can call the LLM instance directly:

```python
response = llm("What is the capital of France?")
print(response)
> Paris
```

### `generate` - Batch Requests

For multiple requests, use `generate`:

```python
prompt = ["What is the capital of France?",  
          "What is the capital of Japan?"]

results = llm.generate(prompt, n=1) 

for result in results.generations:
  print(result.text)
  
> Paris  
> Tokyo
```

## Parameters

You can customize the LLM behavior by passing parameters like:

- `temperature`: Controls randomness, lower values mean more focused responses.
- `top_p`: Alternative to temperature, controls likelihood of unlikely tokens.
- `presence_penalty`: Penalizes new information. Increase to reduce repetition.

For example:

```python 
llm = OpenAI(temperature=0.5, presence_penalty=0.5)
```

See the documentation for each LLM for all available parameters.

## Troubleshooting

- **API Errors:** Invalid API key, rate limit exceeded, etc. Check error message.
- **Timeouts:** Try smaller batches, tweak temperature/top_p. 
- **Failures:** Simplify prompt if too long or confusing.
- **Unsafe content:** Add instructions in prompt to guide response.

## Under the Hood

You can access raw LLM outputs via `llm_output`:

```python
results.llm_output  
```

This contains usage stats and other provider-specific info.


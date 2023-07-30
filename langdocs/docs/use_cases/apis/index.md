# APIs

## Introduction

APIChain allows using large language models (LLMs) to interact with APIs by constructing a chain of the LLM and API docs. By providing a natural language question relevant to the API documentation, APIChain can query the API and retrieve information.

This reference guide will cover:

- Basic usage and setup
- Examples with OpenMeteo, TMDB, ListenNotes and more
- Advanced querying and chaining
- Customizing prompts and parsing

## Basic Usage

To create an APIChain, you need:

- An LLM like OpenAI
- API documentation
- Optional headers if authentication required

```python
from langchain.chains import APIChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

chain = APIChain.from_llm_and_api_docs(llm, api_docs, headers=headers)
```

Construct the chain by passing the LLM, API docs, and optional headers.

Then make queries by running the chain:

```python
response = chain.run("What is the weather in London tomorrow?")
```

## Examples

### OpenMeteo

```python
from langchain.chains.api import open_meteo_docs

chain = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)

response = chain.run('What is the weather like right now in Munich, Germany in degrees Fahrenheit?')
```

This initializes a chain with the OpenMeteo docs. The query asks for the current weather in Munich in Fahrenheit.

### TMDB

```python
import os
os.environ['TMDB_API_KEY'] = "xxx"

from langchain.chains.api import tmdb_docs
headers = {"Authorization": f"Bearer {os.environ['TMDB_API_KEY']}"}

chain = APIChain.from_llm_and_api_docs(llm, tmdb_docs.TMDB_DOCS, headers=headers)

response = chain.run("Search for movies about 'Artificial Intelligence'")
```

This shows using the TMDB API by passing the API key in headers. The chain is constructed with the TMDB docs and used to search for AI movies.

### Listen Notes

```python
import os
listen_api_key = os.environ["LISTEN_API_KEY"]
headers = {"X-ListenAPI-Key": listen_api_key}

from langchain.chains.api import podcast_docs

chain = APIChain.from_llm_and_api_docs(llm, podcast_docs.PODCAST_DOCS, headers=headers)

response = chain.run("Find podcasts about meditation")
```

This initializes a chain with the Listen Notes podcast API, passing the API key. It searches for meditation podcasts.

## Advanced Usage

The examples above show basic single queries. APIChain also supports:

- Chaining multiple APIs by composing chains
- Advanced response parsing with Python
- Caching responses
- Custom prompts for each API
- Error handling

### Chaining Multiple APIs

Chains for different APIs can be composed:

```python
open_meteo_chain = APIChain(llm, open_meteo_docs)
tmdb_chain = APIChain(llm, tmdb_docs, headers)

composed_chain = open_meteo_chain + tmdb_chain

response = composed_chain.run("What's the weather tomorrow in Los Angeles? What are popular movies set in LA?")
```

This composes an OpenMeteo and TMDB chain, allowing querying both APIs.

### Response Parsing

API responses can be parsed in Python before returning:

```python
def parse_response(response):
    data = json.loads(response)
    return data["title"]

chain = APIChain(llm, api_docs, response_parser=parse_response)

title = chain.run("Get title of most popular movie on TMDB")
```

A response parser function can extract the relevant data.

### Custom Prompts

The prompt can be customized per API:

```python
prompt = PromptTemplate(
    input="Question: {question}",
    api_docs=api_docs,
    output="Response: {response}"
)

chain = APIChain(llm, prompt=prompt)
```

This allows modifying the prompt structure.

## Conclusion

In summary, APIChain enables seamless integration of LLMs with APIs using natural language. The examples here covered common use cases and customization techniques. With APIChain, you can leverage the knowledge of large models to query and compose APIs.



# Caching

LangChain provides an optional caching layer for LLMs. This is useful for two reasons:

- It can save you money by reducing the number of API calls you make to the LLM provider, if you're often requesting the same completion multiple times.
- It can speed up your application by reducing the number of API calls you make to the LLM provider.

## In Memory Cache

The in-memory cache keeps a cache in memory for the lifetime of the application. As noted in the reference, "The in-memory cache is useful for simple cases where you just want to cache results during a single run. It does not persist across application restarts."

For example:

```python
from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache() 

# The first time, it is not yet in cache, so it should take longer
llm.predict("Tell me a joke")

# The second time it is, so it goes faster 
llm.predict("Tell me a joke")
```

## SQLite Cache

For caching that persists across runs, SQLite is a good option. As stated in the reference, "The SQLite cache will store results in an SQLite database file, allowing caching to work across application restarts."

For example:

```python
from langchain.cache import SQLiteCache
langchain.llm_cache = SQLiteCache(database_path=".langchain.db")

# The first time, it is not yet in cache, so it should take longer
llm.predict("Tell me a joke") 

# The second time, it loads results from the SQLite database
llm.predict("Tell me a joke")
```

## Optional Caching in Chains

Caching can also be used within chains, where you may want to cache some steps but not others. As noted in the reference, "When creating a chain, you can specify cache=False for any LLMs you want to exclude from caching:"

For example:

```python
cached_llm = OpenAI()
no_cache_llm = OpenAI(cache=False) 

chain = LLMChain(
   llm=cached_llm,
   prompt="...",
   output_parser="..." 
)

# This LLM will be cached  
chain.run(...)   

# This one will not be cached
chain.run(llm=no_cache_llm, ...)
```

This allows customizing caching behavior for different steps as needed.


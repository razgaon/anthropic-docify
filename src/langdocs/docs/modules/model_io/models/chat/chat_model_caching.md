

Caching
=======

LangChain provides an optional caching layer for LLMs. Caching can provide two main benefits:

1. Reduce costs by minimizing API calls to the LLM provider for repeated requests

2. Speed up applications by avoiding unnecessary calls to the LLM provider

There are two main types of caches available in LangChain:

In-Memory Cache
---------------

The in-memory cache keeps a cache in memory while the Python process is running. This is useful for testing or simple use cases:

```python
from langchain.cache import InMemoryCache

llm_cache = InMemoryCache()

# First call is slower as it's not cached 
llm.predict("Tell me a joke")

# Second call is faster from cache
llm.predict("Tell me a joke") 
```

However, the in-memory cache does not persist across sessions.

SQLite Cache
------------

For a persistent cache, SQLite can be used. This caches results to disk in a SQLite database:

```python
from langchain.cache import SQLiteCache

llm_cache = SQLiteCache(database_path=".langchain.db")

# First call slower from cache miss
llm.predict("Tell me a joke")  

# Second call faster from cache hit
llm.predict("Tell me a joke")
```

The SQLite cache persists across sessions and can be configured for optimal performance:

- Set an appropriate cache size based on expected usage patterns
- Configure cache expiration rules to limit stale results
- Optimize database access patterns for frequent queries
- Use serialization to efficiently cache complex object types

The SQLite cache provides a fast, persistent cache optimized for production usage.

Caching in Chains
-----------------

Caching can also be selectively enabled/disabled when using chains:

```python
from langchain.chains import LLMChain

chain = LLMChain(...)

# Disable caching for reduce step 
chain.llm.cache = False
```

This provides flexibility to cache only certain parts of the chain. Construct the full chain first, then modify caching behavior.

Summary
-------

LangChain provides in-memory and SQLite caching to optimize cost and performance. The cache can be configured at the LLM-level or for individual chain steps. Proper caching is a valuable optimization for production applications.

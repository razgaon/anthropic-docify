

# Caching in LangChain

Caching is an important technique in LangChain to improve performance and reduce costs. This guide covers the main caching options, best practices, and advanced usage.

## Overview

LangChain provides two caching mechanisms:

- **In-memory cache:** Fast but ephemeral, cached results disappear when the program ends.
- **SQLite cache:** Persistent cache that works across runs.

Caching stores results keyed on the input text, avoiding redundant calls to the underlying LLM. This saves time and money.

Caching can be disabled for individual nodes when using chains, allowing selective caching.

## Usage Examples

Caching provides significant benefits for real applications:

- In a search engine, cache search results based on the query string.
- In a summarizer, cache summaries for long input documents. 
- In a chatbot, cache responses to common questions.

For example, here is caching used in a summarization pipeline:

```python
from langchain.cache import SQLiteCache

# Persistent cache
langchain.llm_cache = SQLiteCache(".cache") 

# Summarize long document
summary = summarize(long_document) 

# Subsequent calls are fast
summary = summarize(long_document)
```

The first call summarizes normally. Subsequent calls hit the cache instead of rerunning summarization.

## Cache Invalidation

When the underlying data changes, the cache may need to be invalidated. For example:

```python
# Clear the cache when documents are updated
langchain.llm_cache.clear()
```

For SQLiteCache, cache entries automatically expire after a default TTL of 24 hours.

## Cache Sizing

The default SQLiteCache size is 5GB. This provides good performance for many workloads.

For memory-constrained environments, set a lower cache size:

```python 
SQLiteCache(max_cache_size=1_000_000) # 1GB cache
``` 

For large scale production workloads, increase cache size accordingly.

## Conclusion

Caching provides significant speed and cost improvements for LangChain applications. Use in-memory caching for ephemeral caching during a run and SQLite for persistent caching across runs. Cache invalidation and sizing are important considerations for production use cases.


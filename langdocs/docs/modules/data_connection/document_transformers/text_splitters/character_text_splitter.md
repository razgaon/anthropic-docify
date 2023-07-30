

# Text Splitting in LangChain

Text splitting allows processing large documents by breaking them into smaller chunks that fit within the context length of large language models (LLMs). This guide provides an overview of text splitting in LangChain and best practices for optimizing performance.

## Overview

LangChain provides several text splitters to break down documents into consumable chunks for LLMs:

- `CharacterTextSplitter`: Splits on a single character like newlines
- `RecursiveCharacterTextSplitter`: Splits recursively on multiple separators 
- `CodeTextSplitter`: Optimized splitter for source code

Proper text splitting is crucial to maximize context while keeping chunk length reasonable. This guide covers strategies, examples, and parameter tuning guidelines.

## CharacterTextSplitter

The `CharacterTextSplitter` splits text on a single character separator like newlines. 

**How it works**

- Split on a character separator (default `\n\n`)
- Chunk size defined by number of characters

This works well for simple splitting, but more advanced strategies are usually better for complex documents.

**Example: Splitting a book**

```python
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(separator="\n\n", chunk_size=1000)

with open("book.txt") as f:
  book = f.read() 

chunks = splitter.split_text(book)
```

Here the book is split into chunks of 1000 characters on paragraph breaks.

## RecursiveCharacterTextSplitter 

The `RecursiveCharacterTextSplitter` tries splitting recursively on multiple separators like newlines and spaces to keep related content together.

**How it works** 

- Attempts to split on list of separators (`\n\n`, `\n`, ` `, ``)  
- Keeps paragraphs, sentences, words together as long as possible
- Chunk size measured by number of characters

This is the recommended splitter for most text documents.

**Example: Splitting a dataset**

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=2000)

with open("dataset.csv") as f:
  dataset = f.read()
  
chunks = splitter.split_text(dataset)
```

The dataset will be split trying to keep complete rows together.

## CodeTextSplitter

The `CodeTextSplitter` makes it easy to split source code in different languages.

**Supported languages:**

```python
[Language.PYTHON, Language.JAVASCRIPT, Language.SOLIDITY, etc.]
```

Just specify the language and appropriate chunk size.

**Example: Splitting Solidity**

```python 
from langchain.text_splitter import CodeTextSplitter, Language

splitter = CodeTextSplitter(
  language=Language.SOLIDITY, chunk_size=150
)

with open("contract.sol") as f:
  code = f.read()
  
chunks = splitter.split_text(code)
```

The contract will be split trying to keep functions and other logical blocks together.

## Guidelines for Parameter Selection

The main parameters are `chunk_size` and `chunk_overlap`:

- **Chunk size:** Match context length of LLM. For a 2048 token LLM, use 2000 characters.

- **Overlap:** Use 20-50% of chunk size. More overlap provides more context across chunks.

**Examples:**

| Context Length | Chunk Size | Overlap |
|-|-|-|  
| 2048 tokens | 2000 chars | 400 chars |
| 4096 tokens | 4000 chars | 1000 chars |

Some experimentation may be needed to optimize for your use case. Goal is maximize context while keeping chunks consumable.

## Conclusion

Proper text splitting is key to effectively using large documents with LLMs. LangChain provides several robust splitting strategies optimized for different use cases. Tuning parameters like chunk size and overlap based on context length is important for optimal performance.

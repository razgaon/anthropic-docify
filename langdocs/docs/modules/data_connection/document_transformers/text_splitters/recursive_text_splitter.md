

# Recursively Split Text by Characters

The RecursiveCharacterTextSplitter is recommended for splitting generic text into semantically meaningful chunks. It works by recursively trying separator characters to split text until the chunks are small enough.

## How it Works

The RecursiveCharacterTextSplitter tries to split text on a provided list of separator characters, in order. The default separator list is:

```
["\n\n", "\n", " ", ""]
```

This has the effect of trying to keep paragraphs, sentences, and words together in the chunks.

The chunk size is measured by the number of characters. Once the chunks are small enough per the provided chunk size, the splitting stops.

By splitting last on spaces and empty strings, it tries to maintain semantic meaning in each chunk.

## Usage

Import the RecursiveCharacterTextSplitter:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
```

Initialize it with the desired chunk size and overlap:

```python
text_splitter = RecursiveCharacterTextSplitter(
  chunk_size=100,
  chunk_overlap=20,
  length_function=len
)
```

Then split text:

```python 
texts = text_splitter.create_documents([text])
```

You can also customize the separator list:

```python
text_splitter = RecursiveCharacterTextSplitter(
  separators=["\n\n", "\n", " "],
  chunk_size=100,
  chunk_overlap=20,
  length_function=len  
)
```

## Examples

Split a long text file into chunks:

```python
with open('book.txt') as f:
  book = f.read()

texts = text_splitter.create_documents([book])  
```

Get the first few split chunks:

```python  
chunks = text_splitter.split_text(book)[:5]
```

Pass along metadata during splitting:

```python
metadata = {"title": "My Book"}
texts = text_splitter.create_documents([book], metadatas=[metadata])
```

The RecursiveCharacterTextSplitter is useful for splitting long documents into smaller chunks while trying to maintain semantic meaning. It provides flexibility to customize the separator characters and chunk size as needed.


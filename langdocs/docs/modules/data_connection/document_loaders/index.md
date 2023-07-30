

# Document Loaders

Document loaders allow you to load data from various sources into `Document` objects that can be used in LangChain. A `Document` contains the text content as well as any associated metadata. 

There are built-in document loaders for many common data sources like files, web pages, YouTube transcripts, and more. See the [Integrations](/docs/integrations/document_loaders/) page for details on all the available document loader integrations.

## Key Features

The main features of document loaders are:

- **Load**: Load data from a source into `Document` objects
- **Lazy Load**: Lazily load data into memory only when needed
- **Splitting**: Automatically split documents into smaller chunks

## Get Started

The simplest loader reads in a file as text and places it all into one Document:

```python
from langchain.document_loaders import TextLoader

loader = TextLoader("./index.md")  
loader.load()
```

This loads the contents of `index.md` into a single `Document`.

### Lazy Loading

With lazy loading, documents are only loaded from disk when you first request them. This is useful for large datasets where you don't want everything in memory at once. 

You can also iterate over a lazy loader to load each document:

```python
for doc in loader:
    print(doc) 
```

### Splitting Documents

The default recommended text splitter is the RecursiveCharacterTextSplitter. This text splitter takes a list of characters. It tries to create chunks based on splitting on the first character, but if any chunks are too large it then moves onto the next character, and so forth.

To split documents into smaller chunks:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter()

loader = TextLoader("./file.txt", splitter=splitter)
docs = loader.load()
```

Now `docs` will contain multiple `Document` objects split from the original text.

There are many different [text splitting](/docs/text_splitting) strategies available to handle different document types. You can also customize parameters like chunk size and overlap amount.

## Tips for Large Datasets

When working with large volumes of documents:

- Use lazy loading to avoid loading everything into memory
- Load documents in parallel using multiprocessing  
- Split documents into small chunks suitable for your model
- Store embeddings for fast nearest-neighbor search

See the [Vector Stores](/docs/vector_stores) page for more details on efficiently working with large datasets.


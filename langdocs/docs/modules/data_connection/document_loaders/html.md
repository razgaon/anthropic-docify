

# Loading Documents in LangChain

## Overview

LangChain provides utilities for loading various document formats like HTML, Markdown, PDFs, etc. into a common `Document` format that can be used in downstream NLP pipelines. This document provides examples and explanations of the key document loading capabilities in LangChain.

## Loading HTML

[HTML](https://en.wikipedia.org/wiki/HTML) (Hypertext Markup Language) is a standard markup language used to create web pages.

To load an HTML file into a `Document` object in LangChain, we can use the `UnstructuredHTMLLoader`:

```python
from langchain.document_loaders import UnstructuredHTMLLoader

loader = UnstructuredHTMLLoader("example_data/fake-content.html")

data = loader.load()

print(data)
```

This will extract the main textual content from the HTML, cleaning up any markup, and store it in the `page_content` field of the `Document`. The source path will be stored in `metadata`.

```
[Document(page_content='My First Heading\n\nMy first paragraph.',
           metadata={'source': 'example_data/fake-content.html'})]
```

### Loading HTML with BeautifulSoup

We can also use the popular [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse and load HTML through the `BSHTMLLoader`:

```python
from langchain.document_loaders import BSHTMLLoader

loader = BSHTMLLoader("example_data/fake-content.html")
data = loader.load()

print(data)
```

This will extract the text content like the `UnstructuredHTMLLoader`, but also parse out the title of the HTML page and store it in the `metadata`:

```
[Document(page_content='\n\nTest Title\n\n\nMy First Heading\nMy first paragraph.\n\n\n',
           metadata={'source': 'example_data/fake-content.html',
                    'title': 'Test Title'})]
```

The `BSHTMLLoader` provides more control over parsing and extracting content from complex HTML documents.

## Loading Markdown

[Markdown](https://en.wikipedia.org/wiki/Markdown) is a popular lightweight markup language used for formatting plain text documents.

To load a Markdown document, we can use the `UnstructuredMarkdownLoader`:

```python
from langchain.document_loaders import UnstructuredMarkdownLoader

markdown_path = "document.md"
loader = UnstructuredMarkdownLoader(markdown_path)

data = loader.load()
print(data)
```

This will extract all the text content, excluding any Markdown syntax, into the `page_content` field of the `Document`. 

In addition to plain text content, the loader can also retain some structure from the original Markdown document:

```python
loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")

data = loader.load()
print(data[0])
```

```
Document(page_content='# My Document Title',
          metadata={'source': 'document.md',
                   'page_number': 1, 
                   'category': 'Title'})
```

This allows accessing elements like headings, lists, etc separately for further processing.

## Loading PDFs

[PDF](https://en.wikipedia.org/wiki/PDF) (Portable Document Format) is a common format for distributing documents digitally.

To load a PDF file, we can use the `PDFLoader`:

```python
from langchain.document_loaders import PDFLoader

loader = PDFLoader("paper.pdf")
data = loader.load()

print(data[0])
```

```
Document(page_content='Deep learning (DL) has become ubiquitous for document image analysis (DIA) in recent years. However, none of them are optimized for challenges in the domain of DIA. This represents a major gap in the existing toolkit, as DIA is central to academic research across a wide range of disciplines in the social sciences and humanities. This paper introduces LayoutParser, an open-source library for streamlining the usage of DL in DIA research and applications. The core LayoutParser library comes with a set of simple and intuitive interfaces for applying and customizing DL models for layout detection, character recognition, and many other document processing tasks. To promote extensibility, LayoutParser also incorporates a community platform for sharing both pre-trained models and full document digitization pipelines. We demonstrate that LayoutParser is helpful for both lightweight and large-scale digitization pipelines in real-word use cases. The library is publicly available at https://layout-parser.github.io.',
           metadata={'source': 'example_data/layout-parser-paper.pdf',
                    'page_number': 1,
                    'total_pages': 16})
```

This extracts the text content from each page into separate `Document` objects. Metadata like page number is also stored.

## Conclusion

LangChain provides simple utilities like `UnstructuredHTMLLoader`, `BSHTMLLoader`, `UnstructuredMarkdownLoader`, `PDFLoader` to load HTML, Markdown, PDFs, and other text-based documents into a common `Document` format for downstream NLP tasks. The loaders provide options to retain structure and metadata from the original documents when needed.


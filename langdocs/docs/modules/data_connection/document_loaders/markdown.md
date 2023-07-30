

# Loading and Processing Documents with LangChain

## Introduction

LangChain provides powerful tools for loading various document formats like Markdown, HTML, and PDF into a common representation that enables downstream natural language processing tasks. This guide covers the key concepts and includes concrete examples for real-world usage.

## Loading Markdown

Markdown is a popular lightweight markup language used for formatting plain text documents. LangChain provides easy loading of Markdown through the `UnstructuredMarkdownLoader`:

```python
from langchain.document_loaders import UnstructuredMarkdownLoader

markdown_path = "README.md" 
loader = UnstructuredMarkdownLoader(markdown_path)

data = loader.load()
```

The `load()` method parses the Markdown and returns a list of `Document` objects containing the content.

For example, loading the LangChain README:

```python
data

[Document(page_content="# LangChain\n\n🎊 Building applications with LLMs through composability 🎊\n\n...",  
           metadata={'source': 'README.md'})]
```

The `page_content` contains the full extracted text. The `metadata` includes the source path.

## Retaining Markdown Elements

By default, the Markdown is combined into a single text block. To retain the original sections, headers, etc., specify `mode="elements"`:

```python
loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")

data = loader.load()
data[0]

Document(page_content='🎼🤗 LangChain',
          metadata={'source': 'README.md',
                    'page_number': 1, 
                    'category': 'Title'})
```

Now the elements are separated, with metadata like `category` identifying headers, paragraphs, and more.

## Loading HTML

Loading HTML works similarly using `UnstructuredHTMLLoader`:

```python
from langchain.document_loaders import UnstructuredHTMLLoader

loader = UnstructuredHTMLLoader("index.html")
data = loader.load() 
```

This extracts all text from the HTML document.

For more structured extraction, `BSHTMLLoader` uses BeautifulSoup to parse the HTML and capture additional metadata like page titles:

```python
from langchain.document_loaders import BSHTMLLoader

loader = BSHTMLLoader("index.html")
data = loader.load()

print(data[0].metadata['title'])
```

## Loading PDFs

To load PDF documents, LangChain provides the `PyPDFium2Loader`:

```python
from langchain.document_loaders import PyPDFium2Loader

loader = PyPDFium2Loader("paper.pdf")
data = loader.load()
```

This uses the PyPDFium2 library to extract text and metadata from PDFs.

## Real-World Usage

The document loading capabilities of LangChain enable many downstream NLP applications. Here are two concrete examples:

**Search/QA over Papers:** Load a folder of academic papers as PDFs. Then implement a chain that takes questions, searches the paper contents, and returns an extractive answer.

**Summarize Blog Posts:** Load a WordPress site's HTML pages. Summarize each post into a short paragraph to generate a digest.

Some other applications enabled by the loaders:

- Chatbots that load relevant documents to a conversation for more knowledgeable responses.
- Agents that load webpages to extract information from or reason about.

The unified `Document` format returned by the loaders provides a consistent way to bring external data into a LangChain application.

## Limitations

Some limitations to be aware of when loading documents:

- Very large documents may exceed memory constraints. Consider streaming or chunking.
- Complex formats like PDF require additional parsing logic beyond basic text extraction.
- Expect noise and inconsistencies when extracting text from arbitrary web pages.

## Conclusion

LangChain makes it simple to load documents in various formats for downstream NLP tasks. The built-in loaders handle details like Markdown parsing and PDF extraction so you can focus on your core application logic.


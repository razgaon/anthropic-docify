

# Loading PDF Documents

## Table of Contents
- [Introduction](#introduction)
- [Comparing PDF Loading Libraries](#comparing-libraries)
- [Fetching Remote PDFs](#fetching-remote-pdfs) 
- [Page-level Access](#page-level-access)
- [Preserving Text Formatting](#preserving-formatting)  
- [Fast and Accurate Text Extraction](#fast-and-accurate)
- [Conclusion](#conclusion)

## Introduction

Portable Document Format (PDF) is a common file format for presenting documents in a manner independent of application software, hardware, and operating systems.

This guide covers loading PDF documents into the Document format used in LangChain for downstream processing. We will explore various Python libraries that extract text and metadata from PDFs, each with their own advantages.

## Comparing PDF Loading Libraries

There are several popular Python libraries for loading PDFs:

- **PyPDF** can load PDFs into an array of Document objects with page content and metadata. Good for page-level access.
- **MathPix** uses OCR optimized for math/scientific docs. Returns text and LaTeX equations.  
- **Unstructured** focuses on extracting text and tables. Can fetch remote PDFs.
- **PyPDFium2** fast performance but less accurate text extraction.
- **PDFMiner** accurately preserves text formatting, good for HTML parsing.
- **PyMuPDF** and **pdfplumber** provide the best overall text accuracy.

The optimal library depends on your specific needs. See the sections below for more details on each one.

## Fetching Remote PDFs

To load online PDFs, Unstructured provides a simple API:

```python
from langchain.document_loaders import OnlinePDFLoader

url = "https://arxiv.org/pdf/2302.03803.pdf" 
loader = OnlinePDFLoader(url)
data = loader.load()
```

All other PDF loaders can also fetch URLs by passing the URL string instead of a file path.

## Page-level Access 

PyPDF and PyMuPDF both provide access to individual pages:

```python
# PyPDF
pages = loader.load_and_split() 

# PyMuPDF 
loader = PyMuPDFLoader("paper.pdf")
data = loader.load() # Returns 1 Document per page
```

This can be useful for tasks like semantic search over specific pages.

## Preserving Text Formatting

To extract text while preserving formatting, PDFMiner has a HTML mode:

```python
loader = PDFMinerPDFasHTMLLoader("paper.pdf")
content = loader.load()[0].page_content

# Parse HTML 
soup = BeautifulSoup(content, 'html.parser')
```

The HTML can be parsed to access text elements like headings, captions, etc.

## Fast and Accurate Text Extraction

PyMuPDF and pdfplumber provide the most accurate text extraction, while still being fast:

```python
# PyMuPDF
loader = PyMuPDFLoader("paper.pdf")
data = loader.load()

# pdfplumber 
loader = PDFPlumberLoader("paper.pdf")
data = loader.load() 
```

Both return detailed metadata in addition to the text content.

## Conclusion

There are many good PDF loading options in Python. Choose based on your specific needs - page access, accuracy, text formatting, etc. PyMuPDF and pdfplumber are great general-purpose libraries. See the LangChain documentation for code examples of each.

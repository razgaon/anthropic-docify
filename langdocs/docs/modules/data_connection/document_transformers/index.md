

# Document Transformers

Document transformers allow you to manipulate and modify documents in various ways before passing them to your LLM. This guide provides examples and details on the built-in document transformers in LangChain.

## Text Splitting

When dealing with long text, it is often necessary to split it into smaller chunks that can fit into your model's context window. LangChain provides text splitters to handle this.

The default text splitter is `RecursiveCharacterTextSplitter`. It recursively tries splitting text on newline characters, spaces, and empty strings until the chunks are small enough. You can customize the splitting behavior by configuring:

- `chunk_size` - The maximum chunk size 
- `chunk_overlap` - Amount of overlap between chunks
- `length_function` - How to measure chunk length (e.g. number of tokens)

Here is an example of splitting a long text document into smaller chunks:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=100) 

docs = splitter.create_documents([BIG_TEXT]) 
```

### Splitting Code

To split code, use the `CodeTextSplitter` class. It splits code based on language-specific syntax and structure.

Import the splitter and `Language` enum:

```python
from langchain.text_splitter import CodeTextSplitter, Language
```

Create a splitter for your desired language:

```python
python_splitter = CodeTextSplitter(
  language=Language.PYTHON, 
  chunk_size=50
)
```

Then pass your code to `create_documents`:

```python
python_docs = python_splitter.create_documents([PYTHON_CODE])
```

This will return a list of `Document` objects with the split code.

Here is an example for JavaScript:

```python
js_splitter = CodeTextSplitter(
  language=Language.JS,
  chunk_size=60  
)

js_docs = js_splitter.create_documents([JS_CODE])
```

And for Markdown:

```python 
md_splitter = CodeTextSplitter(
  language=Language.MARKDOWN,
  chunk_size=60
)

md_docs = md_splitter.create_documents([MARKDOWN_TEXT])
```

## Other Transformations

In addition to splitting, LangChain provides other useful document transformers:

- `EmbeddingsRedundantFilter` - Removes duplicate/redundant documents based on semantic similarity.

- `doctran` - An integration for translating documents between languages, extracting metadata, and converting documents to QA format.

Some examples:

```python
from langchain.filters import EmbeddingsRedundantFilter

filter = EmbeddingsRedundantFilter()
filtered_docs = filter.filter(docs)
```

```python
import doctran

translator = doctran.Translator() 
french_docs = translator.translate(english_docs, target_language='fr')
```

In summary, LangChain provides a variety of document transformers to manipulate text before passing it to your LLM. The text splitters allow splitting long documents and code, while other tools like doctran enable translation, QA conversion, and more.


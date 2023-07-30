

# Loading Documents from a Directory

The `DirectoryLoader` provides a convenient way to recursively load text files from a directory into `Document` objects using a specified loader class. It takes a root path and glob pattern to match files to load.

## Overview

The key features of the `DirectoryLoader` include:

- Recursively loads files matching a glob pattern
- Applies a loader class like `TextLoader` or `PythonLoader` to each file
- Can skip errors and continue loading valid files
- Option to auto-detect encodings before raising decode errors
- Supports multithreading and progress bars

## Usage

To load `.md` files with default settings:

```python
from langchain.document_loaders import DirectoryLoader

loader = DirectoryLoader('../', glob="**.md")
docs = loader.load()
```

To load `.py` files using the `PythonLoader`:

```python
from langchain.document_loaders import DirectoryLoader, PythonLoader 

loader = DirectoryLoader('../../../../../', glob="**.py", loader_cls=PythonLoader)
docs = loader.load()
```

## Handling Errors

By default, any file error fails the entire load. 

To continue loading valid files on error:

```python
loader = DirectoryLoader(path, silent_errors=True)
docs = loader.load() 
```

To auto-detect encodings before decode errors:

```python
text_loader_kwargs={'autodetect_encoding': True}
loader = DirectoryLoader(
  path,
  loader_cls=TextLoader, 
  loader_kwargs=text_loader_kwargs
)
docs = loader.load()
```

## Conclusion

The `DirectoryLoader` provides a flexible way to load text files from directories into documents. Its configurability around error handling and encodings makes it robust for real-world usage.


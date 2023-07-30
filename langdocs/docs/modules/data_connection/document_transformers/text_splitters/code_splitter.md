

# Splitting Code with LangChain

The `CodeTextSplitter` in LangChain provides a convenient way to split code into smaller pieces for feeding into large language models (LLMs) by auto-detecting the programming language syntax. This allows breaking up large code files into manageable chunks while preserving structure.

## Usage

Import the `CodeTextSplitter` and `Language` enum:

```python
from langchain.text_splitter import CodeTextSplitter, Language
```

Create a splitter by specifying the language: 

```python 
python_splitter = CodeTextSplitter(language=Language.PYTHON)
```

See the [full list of supported languages](https://docs.langchain.dev/en/latest/api-reference/text-splitters#languagelanguage).

### Customization

You can customize the splitter by setting the:

- `chunk_size`: Maximum chunk length 
- `overlap`: Number of characters to overlap between chunks
- `separators`: List of custom separators 

For example:

```python
python_splitter = CodeTextSplitter(
  language=Language.PYTHON,
  chunk_size=100,
  overlap=20,
  separators=["\n\n", "\nclass"]  
)
```

See the [API docs](https://docs.langchain.dev/en/latest/api-reference/text-splitters.html#codetextsplitter) for more details.

## Examples

Here are examples splitting code in different languages:

### Python

```python
python_code = """
def hello_world():
  print("Hello World!")
  
hello_world()  
"""

python_docs = python_splitter.split(python_code)
```

### Java

```java
String helloWorld = "Hello World!";

System.out.println(helloWorld);
```

### PHP

```php

```

### Go

```go
package main

import "fmt"

func main() {
  fmt.Println("Hello World!") 
}
``` 

The splitter handles comments, strings, and code structure intelligently for each language.

## Comparison to Other Splitters

The CodeTextSplitter is specialized for source code, compared to general purpose splitters like the RecursiveCharacterTextSplitter. It understands language syntax to split logically while preserving structure.

For non-code text, use a general splitter. For code, the CodeTextSplitter is recommended.

## Conclusion

The CodeTextSplitter provides an easy way to split source code for feeding into LLMs in an intelligent, language-aware manner. With support for many languages and customizable options, it is a valuable tool for working with large codebases.

See the [API documentation](https://docs.langchain.dev/en/latest/api-reference/text-splitters.html#codetextsplitter) for additional details.

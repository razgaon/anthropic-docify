

# JSONLoader Documentation 

## Introduction

The JSONLoader enables importing large JSON and JSONL datasets into LangChain for NLP tasks. It provides flexible parsing of JSON data into Document objects using jq query syntax.

## Usage

To load documents from a JSON file:

```python
from langchain.document_loaders import JSONLoader

loader = JSONLoader(
    file_path='data.json',
    jq_schema='.messages[].content'  
)

docs = loader.load()
```

For a JSON Lines file:

```python
loader = JSONLoader(
    file_path='data.jsonl', 
    jq_schema='.text',
    json_lines=True
)
```

The jq_schema specifies where to extract the document content from the JSON structure.

### Realistic Example

Here is an example JSON structure from a typical social media dataset:

```json
{
  "post_id": "1234", 
  "text": "Hello world!",
  "user": {
    "name": "John Doe",
    "handle": "@john"
  },
  "timestamp": 1578954621
}
```

To extract just the text, we can use:

```python
jq_schema='.text'
```

## Metadata Extraction

We can also extract metadata from the JSON:

```python
def metadata_func(record, metadata):
  metadata['user'] = record['user']['name']
  
  return metadata
  
loader = JSONLoader(
  jq_schema='.text',
  metadata_func=metadata_func  
)
```

The metadata_func has full control over the metadata format.

## Advanced Usage

The jq_schema can query complex nested JSON structures:

```
JSON -> {"key": {"nested": [{"text": ...}, {"text": ...}]}}
jq_schema -> ".key.nested[].text" 

JSON -> {"posts": [{"id": ..., "text": ...}, {"id": ..., "text": ...}]} 
jq_schema -> ".posts[].text"
```

For large datasets, use multiprocessing:

```python
loader = JSONLoader(
  file_path='large_data.json',
  jq_schema='.text',
  workers=8
)
``` 

Chunking can also help for memory-constrained environments.

## Conclusion

The JSONLoader provides flexible parsing of JSON data into Documents. The jq syntax gives control over handling varying schemas. Features like metadata extraction and multiprocessing enable importing large JSON datasets for NLP tasks in LangChain.


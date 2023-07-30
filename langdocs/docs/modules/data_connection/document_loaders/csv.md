

# Loading CSV Data in LangChain

## Introduction

Comma-separated values (CSV) files are a ubiquitous format for storing tabular data like spreadsheets or databases. LangChain provides the `CSVLoader` class to enable loading CSV data into `Document` objects that can be used in chains. The `CSVLoader` handles splitting the CSV into rows and adding metadata like row numbers and file paths automatically. This guide covers how to use the `CSVLoader` to load CSVs in various formats and customize the parsing.

## Basic Usage

The simplest way to load a CSV is:

```python
from langchain.document_loaders import CSVLoader

loader = CSVLoader('data.csv')
docs = loader.load()
```

This will create one `Document` per row using the CSV file path as the `source` metadata. 

For example, loading a CSV of baseball team stats:

```python
docs = CSVLoader('mlb_stats.csv').load()
```

Would create documents like:

```
Document(page_content='Team: Yankees\nWins: 95', 
         source='mlb_stats.csv', row=2)
```

## Customizing Parsing

You can pass arguments to `CSVLoader` to control how the CSV is parsed:

```python 
loader = CSVLoader('data.csv', csv_args={
    'delimiter': '\t',
    'quotechar': "'",
    'fieldnames': ['Date', 'Value']
})
```

This uses the Python [csv module](https://docs.python.org/3/library/csv.html) - refer to its docs for all available options.

For example, to load a TSV file:

```python
loader = CSVLoader('data.tsv', csv_args={'delimiter': '\t'})
```

## Setting Source Metadata

By default, the `source` of each document is the original CSV file path. 

To set the source from a column value instead:

```python
loader = CSVLoader('data.csv', source_column='Date')
```

This is useful for chains that lookup answers by source.

For example, loading log files by date:

```python 
loader = CSVLoader('logs.csv', source_column='Date')
```

Would create documents like: 

```
Document(page_content='Error: File not found',
         source='2022-01-01', row=5)
```

## Examples

Here are some examples loading CSVs in different formats:

```python
# Stock market data
loader = CSVLoader('stocks.csv', source_column='Date') 

# Log files with custom delimiter
loader = CSVLoader('logs.csv', csv_args={'delimiter': ' '})

# MLB stats with named columns 
loader = CSVLoader('mlb_stats.csv', 
                   csv_args={'fieldnames': ['Team', 'Wins']})
```

## Conclusion

The `CSVLoader` provides a flexible way to load CSV data into LangChain `Document` objects. By customizing the parser arguments and source metadata, it can handle many CSV formats and use cases. Refer to the [csv module](https://docs.python.org/3/library/csv.html) docs for additional parsing options.

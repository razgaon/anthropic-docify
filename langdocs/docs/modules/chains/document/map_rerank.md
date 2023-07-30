

# Map Re-rank

The map re-rank documents chain runs an initial prompt on each document that not only tries to complete a task but also gives a score for how certain it is in its answer. The highest scoring response is returned.

## How It Works

The map re-rank chain takes in a list of documents. For each document, it runs a prompt that is designed to:

1. Complete a specific task like answering a question or summarizing text 
2. Generate a confidence score representing how certain the model is in its response

For example, the prompt could be:

```
Answer the question below and rate your confidence from 1-10: 

Question: {question}

Response:
Confidence: 
```

The response with the highest confidence score is then returned as the final output. This allows the chain to select the response that the model is most confident in. 

## Usage

Here is an example of how to use the map re-rank chain:

```python
docs = [...] # list of documents
prompt = PromptTemplate(template="...") 

chain = MapReRankDocumentsChain(llm=llm, prompt=prompt)

output = chain.run(docs)
```

The prompt template and LLM can be customized as needed. Parameters like temperature and frequency penalty can also be configured.

## Prompt Engineering

Constructing effective prompts is key to successfully using the map re-rank chain. Here are some best practices:

- Clearly separate the response generation from the confidence scoring in the prompt
- Use a numerical scale like 1-10 for confidence scoring
- Tune parameters like temperature to optimize prompt engineering
- Test different prompt formats and styles

## Examples

### Question Answering

Prompt template:

```
Answer the question below and rate your confidence from 1-10:

Question: {question}

Response:  
Confidence: 
```

### Summarization

Prompt template:

```
Summarize this text in one sentence and rate your confidence from 1-10:

{text}

Summary:
Confidence:  
```

The map re-rank chain allows customization of prompts for different tasks. The key is generating both a response and associated confidence score.


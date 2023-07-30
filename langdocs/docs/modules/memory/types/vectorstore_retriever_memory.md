

Vector store-backed memory
==========================

`VectorStoreRetrieverMemory` stores memories in a VectorDB and queries the top-K most "salient" docs every time it is called. 

This differs from most of the other Memory classes in that it doesn't explicitly track the order of interactions.

In this case, the "docs" are previous conversation snippets. This can be useful to refer to relevant pieces of information that the AI was told earlier in the conversation.

### Initialize your VectorStore

Depending on the store you choose, this step may look different. Consult the relevant VectorStore documentation for more details.

Here are some examples initializing different types of vector stores:

```python
import faiss  

from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings  
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
  
# Load the document, split it into chunks, embed each chunk and load it into the vector store.  
raw_documents = TextLoader('../../../state_of_the_union.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = FAISS.from_documents(documents, OpenAIEmbeddings())
```

```python
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings   
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Annoy

raw_documents = TextLoader('../../../state_of_the_union.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)   
documents = text_splitter.split_documents(raw_documents)

embeddings = OpenAIEmbeddings()
db = Annoy.from_documents(documents, embeddings) 
```

See the [Vector Stores documentation](/docs/integrations/vectorstores) for more details on initializing different types of vector stores like Weaviate, Pinecone, etc.

### Create your the VectorStoreRetrieverMemory

The memory object is instantiated from any VectorStoreRetriever.

```python
# In actual usage, you would set `k` to be a higher value, but we use k=1 to show that  
# the vector lookup still returns the semantically relevant information  
retriever = vectorstore.as_retriever(search_kwargs=dict(k=1))
memory = VectorStoreRetrieverMemory(retriever=retriever)
  
# When added to an agent, the memory object can save pertinent information from conversations or used tools
memory.save_context({"input": "My favorite food is pizza"}, {"output": "that's good to know"})
memory.save_context({"input": "My favorite sport is soccer"}, {"output": "..."}) 
memory.save_context({"input": "I don't the Celtics"}, {"output": "ok"})
```

### Best practices for setting k

When initializing the `VectorStoreRetrieverMemory`, the `k` parameter controls how many of the most relevant memories will be retrieved each time the memory is queried. Here are some best practices for setting `k` based on your use case:

- For a digital assistant use case with longer conversations, set `k` between 5-10 to provide enough context from the conversation history.

- For a QA use case with many short questions/answers, set `k` between 1-3 to avoid retrieving too much irrelevant information. 

- For open-domain conversations, start with a higher `k` (10+) and tune down if the model starts repeating itself or retrieving irrelevant memories.

- When in doubt, start on the higher end for `k` and tune down based on the quality and relevance of retrieved memories. 

- Consider the computational resources available - higher `k` means more embeddings to compute, so balance performance vs. quality of results.

### Using in a chain

Let's walk through an example, again setting `verbose=True` so we can see the prompt.

```python
llm = OpenAI(temperature=0) # Can be any valid LLM

_DEFAULT_TEMPLATE = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
  
Relevant pieces of previous conversation:  
{history}
  
(You do not need to use these pieces of information if not relevant)
  
Current conversation:  
Human: {input}
AI:"""

PROMPT = PromptTemplate(
  input_variables=["history", "input"], template=_DEFAULT_TEMPLATE  
)

conversation_with_summary = ConversationChain(
  llm=llm,    
  prompt=PROMPT,
  # We set a very low max_token_limit for the purposes of testing.
  memory=memory,
  verbose=True
)
```

Here is an example conversation demonstrating how the memory tracks context across multiple turns:

```python
conversation_with_summary.predict(input="Hi, my name is Perry, what's up?")

conversation_with_summary.predict(input="I love playing soccer")

conversation_with_summary.predict(input="What's my favorite sport?") 
```

This shows how the memory is used to track the context that soccer is the user's favorite sport across multiple turns of the conversation.


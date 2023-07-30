Vector store-backed retriever
=============================

A vector store retriever is a retriever that uses a vector store to retrieve documents. It is a lightweight wrapper around the Vector Store class to make it conform to the Retriever interface.
It uses the search methods implemented by a vector store, like similarity search and MMR, to query the texts in the vector store.

Once you construct a Vector store, it's very easy to construct a retriever. Let's walk through an example.


```
from langchain.document\_loaders import TextLoader  
loader = TextLoader('../../../state\_of\_the\_union.txt')  

```

```
from langchain.text\_splitter import CharacterTextSplitter  
from langchain.vectorstores import FAISS  
from langchain.embeddings import OpenAIEmbeddings  
  
documents = loader.load()  
text\_splitter = CharacterTextSplitter(chunk\_size=1000, chunk\_overlap=0)  
texts = text\_splitter.split\_documents(documents)  
embeddings = OpenAIEmbeddings()  
db = FAISS.from\_documents(texts, embeddings)  

```

```
 Exiting: Cleaning up .chroma directory  

```

```
retriever = db.as\_retriever()  

```

```
docs = retriever.get\_relevant\_documents("what did he say about ketanji brown jackson")  

```
Maximum Marginal Relevance Retrieval[​](#maximum-marginal-relevance-retrieval "Direct link to Maximum Marginal Relevance Retrieval")
------------------------------------------------------------------------------------------------------------------------------------

By default, the vectorstore retriever uses similarity search. If the underlying vectorstore support maximum marginal relevance search, you can specify that as the search type.


```
retriever = db.as\_retriever(search\_type="mmr")  

```

```
docs = retriever.get\_relevant\_documents("what did he say about ketanji brown jackson")  

```
Similarity Score Threshold Retrieval[​](#similarity-score-threshold-retrieval "Direct link to Similarity Score Threshold Retrieval")
------------------------------------------------------------------------------------------------------------------------------------

You can also a retrieval method that sets a similarity score threshold and only returns documents with a score above that threshold


```
retriever = db.as\_retriever(search\_type="similarity\_score\_threshold", search\_kwargs={"score\_threshold": .5})  

```

```
docs = retriever.get\_relevant\_documents("what did he say about ketanji brown jackson")  

```
Specifying top k[​](#specifying-top-k "Direct link to Specifying top k")
------------------------------------------------------------------------

You can also specify search kwargs like `k` to use when doing retrieval.


```
retriever = db.as\_retriever(search\_kwargs={"k": 1})  

```

```
docs = retriever.get\_relevant\_documents("what did he say about ketanji brown jackson")  

```

```
len(docs)  

```

```
 1  

```

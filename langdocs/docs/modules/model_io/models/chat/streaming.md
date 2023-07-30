

Streaming
=========

Some Chat models provide a streaming response. This means that instead of waiting for the entire response to be returned, you can start processing it as soon as it's available. This is useful if you want to display the response to the user as it's being generated, or if you want to process the response as it's being generated.

Currently, we support streaming for a broad range of Chat model implementations, including but not limited to `ChatOpenAI` and `ChatAnthropic`. To utilize streaming, use a [`CallbackHandler`](https://github.com/hwchase17/langchain/blob/master/langchain/callbacks/base.py) that implements `on_chat_new_message`. 

### Displaying Streaming Results

One way to use streaming is to print out the results in real-time. Here is an example using `StreamingStdOutCallbackHandler`:

```python
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
resp = chat([HumanMessage("Write me a song about sparkling water.")])
```

This will print the song lyrics as they are generated.

### Persisting Streaming Results 

Another common use case is to persist the streaming results to a database or file storage. Here is an example saving the chat history to SQLite:

```python
import sqlite3
from langchain.callbacks.base import CallbackHandler

class ChatHistoryCallback(CallbackHandler):

    def __init__(self):
        self.conn = sqlite3.connect('chat_history.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE chathistory
            (id INTEGER PRIMARY KEY, role TEXT, content TEXT)''')

    def on_chat_new_message(self, message):
        self.c.execute("INSERT INTO chathistory VALUES (NULL, ?, ?)",  
                       (message.role, message.content))
        self.conn.commit()

# Usage:
chat = ChatOpenAI(streaming=True, callbacks=[ChatHistoryCallback()])
chat([HumanMessage("Hello!")]) 
```

When persisting results, be mindful of potential bottlenecks. If the chat model generates messages faster than your database can ingest, you may need queueing, buffering, or rate limiting.

### Real-time NLP

You can also process each message as it streams in to enable real-time NLP. For example, you could perform sentiment analysis on each chat message and aggregate the results.

### Exposing via HTTP

Finally, you can build web APIs by exposing the `CallbackHandler` through a web framework like FastAPI. This allows streaming messages to clients over HTTP.

This allows you to build powerful applications on top of streaming chat models!


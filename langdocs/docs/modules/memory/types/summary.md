

# Conversation Summary Memory

ConversationSummaryMemory is a type of memory in LangChain that creates a summary of the conversation over time. This can be useful for condensing long conversations into succinct summaries, rather than including the full verbose message history in the prompt.

## How it Works

Under the hood, ConversationSummaryMemory utilizes an LLM to generate summaries. As new messages are added to the conversation, the LLM will generate a new summary incorporating the new information. This summary is then stored in memory and can be injected into prompts.

For example:

```python
from langchain.memory import ConversationSummaryMemory
from langchain.llms import OpenAI

memory = ConversationSummaryMemory(llm=OpenAI()) 

memory.add_user_message("Hello!")
memory.add_ai_message("Hi there!")

print(memory.get_summary())

> "The human greeted the AI, and the AI responded in a friendly manner." 
```

## When to Use It

ConversationSummaryMemory is most useful for long, multi-turn conversations where keeping the full verbose message history would take up too many tokens. The summarization allows condensing these long conversations into succinct summaries that still capture the core semantic information.

It is less useful for short conversations, where the full message history may fit within token limits.

## Examples

### Long Conversation Example

Here is an example of using ConversationSummaryMemory on a longer conversation:

```python
memory = ConversationSummaryMemory(llm=OpenAI())

memory.add_user_message("Hello! How are you doing today?")  
memory.add_ai_message("I'm doing great, thanks for asking!")

memory.add_user_message("That's good to hear. What have you been up to lately?")
memory.add_ai_message("I've been having some interesting conversations and learning new things. How about you?") 

memory.add_user_message("I've been pretty busy with work and family. But it's good to take a break and chat.")
memory.add_ai_message("I agree, it's important to take breaks. I'm always here if you need someone to chat with!")

print(memory.get_summary())

> "The human greeted the AI and asked how it was doing. The AI responded positively. The human asked what the AI had been up to, and the AI discussed some of its recent conversations and learning. The human talked about being busy with work and family. The AI agreed on the importance of taking breaks."
```

This demonstrates how ConversationSummaryMemory can condense a longer conversation into a concise summary.

### Short Conversation Example

For a short conversation, the full message history may be short enough to include directly:

```python
memory = ConversationSummaryMemory(llm=OpenAI())

memory.add_user_message("Hello!")
memory.add_ai_message("Hi there!")

print(memory.get_messages())

> ["Hello!", "Hi there!"] 
```

So for short conversations, it may not provide much benefit over just using the full message history.

## Tuning

There are a few hyperparameters that can be tuned on the summarization model:

- **Temperature**: Lower temperature (e.g. 0.3) leads to more deterministic summaries focused on key details. Higher temperature (e.g. 1) leads to more diverse summaries.
- **Top-k/Top-p**: Lower top-k/top-p values like 10/0.3 will produce more focused summaries with fewer extraneous details.

Some good starting values to try:

- Long conversations: temperature=0.3, top-k=10, top-p=0.3 
- Short conversations: temperature=1, top-k=100, top-p=1

## Memory Size Limitations

Since ConversationSummaryMemory utilizes an LLM to generate summaries, it is subject to token limitations. The maximum length of the summary it can produce is determined by the maximum token length supported by the underlying LLM.

To avoid errors from exceeding token limits, you may need to periodically reset the memory after a certain number of turns. For example:

```python
memory = ConversationSummaryMemory(llm=OpenAI(), max_turns=10) 

for turn in range(100):
  
  if turn % 10 == 0:
    memory.reset()
  
  # Add user/ai messages
  # Generate summary
```

This resets the memory every 10 turns to avoid the summaries becoming too long.

The optimal reset frequency depends on the length of your typical conversations versus the maximum token length.

## Initializing from Existing Messages

If you already have a conversation history outside of ConversationSummaryMemory, you can initialize it directly from a list of messages:

```python
from langchain.memory import ConversationSummaryMemory, ChatMessageHistory

history = ChatMessageHistory()
history.add_user_message("Hello!")  
history.add_ai_message("Hi there!")

memory = ConversationSummaryMemory.from_messages(
   chat_memory=history
)
```

## Usage in Chains

ConversationSummaryMemory can be seamlessly integrated into chains. For example:

```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

chain = ConversationChain(
   memory=ConversationSummaryMemory()   
)
```

The summary will automatically be included in the prompt for each prediction.

## Summary

In summary, ConversationSummaryMemory is useful for condensing long conversations into succinct summaries that capture the core information. It works by utilizing an LLM to generate summaries, and can be easily incorporated into LangChain chains. Proper tuning of hyperparameters can help optimize performance, and resetting the memory periodically can avoid exceeding token limitations.


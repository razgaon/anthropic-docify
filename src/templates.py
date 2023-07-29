"""
Human v.s. Assistant

Instructions basics:
- Describe a task, its rules and any exceptions.
- Give example inputs & outputs
- Provide more context
- Demand specific output formatting
- Provide the specific input to process


"""

INITIAL_CRITIQUE_PAGE_TEMPLATE=""""
You are an expert in Langchain, a framework for developing applications powered by large language models. 

Goal: I will provide you with a documentation page on the topic from the reference page. Please review the documentation and official Langchain documentation below, then provide constructive feedback on how 
the documentation can be improved. Focus on providing the top 3 areas for improvement. Ensure your feedback is clear and actionable.

Here are some criteria you should consider when reviewing and critiquing the documentation:
1. Completeness: Is the documentation covering all necessary aspects from the reference page? Are there missing sections that need to be filled in?
2. Clarity: Is the information provided clear and easy to understand? Does the language used make the content accessible to both novice and experienced developers?
3. Technical Accuracy: Are the provided instructions, examples, and other technical details accurate? Are there discrepancies between the context and the official Langchain documentation?
4. Consistency: Is the style and tone of the documentation consistent with the official Langchain documentation? Consistency in language and presentation helps to maintain a unified user experience.
5. Organization and Structure: Is the information presented in a logical and structured manner? Does the flow of content make sense? Is there a table of contents or other navigation aids?
6. Relevance and Usefulness of Examples: Are the examples relevant and do they clearly demonstrate the concept or feature they are meant to explain? Do the examples cover a range of simple to complex scenarios?
7. Grammar and Language Use: Are there grammatical errors or awkward phrasing that makes the documentation hard to understand? Are technical terms explained or linked to further reading?

Context
{reference_page} 

--------

Official documentation:
{reference_page}

Now, provide the top 3 areas for improvement. Ensure your feedback is clear and actionable:
1. 
2. 
3.

"""

IMPROVE_PAGE_TEMPLATE = """
Goal: You are an expert AI agent developer who is tasked with writng comprehensive guides for your library, LangChain. 

You are given context, a reference page, and critique. You need to rewrite the reference page. You are tasked to create a new markdown page that improves on the reference page by achieving the following targets:
Targets:
1. Adding context and relevant information from the provided context. For example, if you reference a topic, bring examples and explanations from the context to the reference page.
2. Providing more detailed explanations of concepts. For example, if the reference page provides a high-level overview of a concept, provide more details and clarity.
3. Adding code examples where applicable. For example, if the reference page provides a code snippet, add more code examples to illustrate the concept.
4. Ensuring a logical structure and clear organization. For example, if the reference page is not well-structured, re-organize the content into a logical order.
5. Using consistent formatting and markdown syntax. For example, if the reference page uses inconsistent formatting, ensure consistent formatting and markdown syntax.
6. Ensuring a clear intro/overview and conclusion/summary. For example, if the reference page does not have a clear intro/overview and conclusion/summary, add one.

Steps:
1. Carefully read through the context and reference page
2. Identify key concepts, explanations, examples in the reference page
3. Supplement these with relevant information, examples from the context
4. Expand explanations of concepts with more details and clarity
5. Add code examples where applicable to illustrate concepts
6. Structure sections and content in a logical order  
7. Use consistent formatting, markdown headers, code blocks
8. Ensure a clear intro/overview and conclusion/summary

Remember, you should output the page in markdown format.

CONTEXT: 
{context}

-----

REFERENCE PAGE:
{reference_page}

-----

CRITIQUE: 
{critique}


Remember to add detailed examples, explanations, and code snippets where applicable. Ensure a logical structure and clear organization. Use consistent formatting and markdown syntax. Ensure a clear intro/overview and conclusion/summary.
Be very detailed and write at least 500 words unless there is nothing to write about.
Start.
"""

# TOOD: Context and examples 
CRITIQUE_PAGE_TEMPLATE = """"
You are an expert in Langchain, a framework for developing applications powered by large language models. 

Goal: I will provide you with draft documentation on the topic from the reference page. Please review the draft documentation and official Langchain documentation below, then provide constructive feedback on how 
the draft documentation can be improved. Focus on providing the top 3 areas for improvement. Ensure your feedback is clear and actionable.

Here are some criteria you should consider when reviewing and critiquing the documentation:
1. Completeness: Is the documentation covering all necessary aspects from the reference page? Are there missing sections that need to be filled in?
2. Clarity: Is the information provided clear and easy to understand? Does the language used make the content accessible to both novice and experienced developers?
3. Technical Accuracy: Are the provided instructions, examples, and other technical details accurate? Are there discrepancies between the draft documentation and the official Langchain documentation?
4. Consistency: Is the style and tone of the documentation consistent with the official Langchain documentation? Consistency in language and presentation helps to maintain a unified user experience.
5. Organization and Structure: Is the information presented in a logical and structured manner? Does the flow of content make sense? Is there a table of contents or other navigation aids?
6. Relevance and Usefulness of Examples: Are the examples relevant and do they clearly demonstrate the concept or feature they are meant to explain? Do the examples cover a range of simple to complex scenarios?
7. Grammar and Language Use: Are there grammatical errors or awkward phrasing that makes the documentation hard to understand? Are technical terms explained or linked to further reading?

Draft documentation:
{improved_page}

Official Langchain documentation:
{reference_page} 

Now, provide the top 3 areas for improvement. Ensure your feedback is clear and actionable:
1. 
2. 
3.
"""


CHECK_MISSING_SYMBOLS_TEMPLATE = """
You are an experienced software engineer. Help review the draft documentation and check if there are any symbols being used that is not imported or defined in the code sample.

Following is the first example:

<example>
For the following code snippet:
```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory()
)

conversation.run("Answer briefly. What are the first 3 colors of a rainbow?")
```

The ConversationChain is initialized with llm=chat, but chat is not defined or imported anywhere in the code. So this would throw an error unless chat was defined and initialized somewhere else in the full code.
</example>

Following is the second example:
<example>
For the following code snippet:
```python
llm = OpenAI(temperature=0)
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain

template = "some template .... {history} {input}"
prompt = PromptTemplate(input_variables=["history", "input"], template=template)
conversation_with_kg = ConversationChain(
    llm=llm, verbose=True, prompt=prompt, memory=ConversationKGMemory(llm=llm)
)
```

The symbol `OpenAI` is used without being imported or defined anywhere in the code. So this would throw an error.
</example>

Here is the draft documentation for you to review:

<draft_documentation>
{draft_documentation}
</draft_documentation>

Now, review the draft documentation and check if there are any symbol being used that is not imported or defined in the code sample. 
For each symbol being used that is not imported or defined, find exact quote from the draft documentation and explain why it is not imported or defined.
If no variable is used without imported or defined, just tell me that there are no variables used without being imported or defined.
"""
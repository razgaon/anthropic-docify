# The following is a template for generating improved documentation markdown pages from context and a reference page

# Context - Provide summary and relevant information from existing documentation pages as context
context = """
"""

# Reference Page - Provide the reference documentation page to improve on  
reference_page = """
""" 

# Improved Page - Generate a new markdown page that improves on the reference page by:
# - Incorporating relevant information and examples from the context
# - Providing more detailed explanations of concepts  
# - Adding code examples where applicable
# - Ensuring a logical structure and clear organization
# - Using consistent formatting and markdown syntax
improved_page = """
Goal: You are an expert AI agent developer who is tasked with writng comprehensive guides for your library, LangChain. 
You are given a context and a reference page to improve on. You are tasked to create a new markdown page that improves on the reference page by:
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

Remember, you should output the page in markdown format. Start.
"""

critique_page = """"
You are an expert in Langchain, a framework for developing applications powered by large language models. 

Goal: I will provide you with draft documentation on the topic of {topic}. Please review the draft documentation and official Langchain documentation below, then provide constructive feedback on how 
the draft documentation can be improved. Focus on providing the top 3 areas for improvement. Ensure your feedback is clear and actionable.

Here are some criteria you should consider when reviewing and critiquing the documentation:
1. Completeness: Is the documentation covering all necessary aspects of using Langchain for Question Answering? Are there missing sections that need to be filled in? For example, installation, getting started, tutorials, API references, examples, etc.
2. Clarity: Is the information provided clear and easy to understand? Does the language used make the content accessible to both novice and experienced users?
3. Technical Accuracy: Are the provided instructions, examples, and other technical details accurate? Are there discrepancies between the draft documentation and the official Langchain documentation?
4. Consistency: Is the style and tone of the documentation consistent with the official Langchain documentation? Consistency in language and presentation helps to maintain a unified user experience.
5. Organization and Structure: Is the information presented in a logical and structured manner? Does the flow of content make sense? Is there a table of contents or other navigation aids?
6. Relevance and Usefulness of Examples: Are the examples relevant and do they clearly demonstrate the concept or feature they are meant to explain? Do the examples cover a range of simple to complex scenarios?
7. Grammar and Language Use: Are there grammatical errors or awkward phrasing that makes the documentation hard to understand? Are technical terms explained or linked to further reading?

Draft documentation:
{draft_documentation}

Official Langchain documentation:
{official_documentation} 

Now, provide the top 3 areas for improvement. Ensure your feedback is clear and actionable:
1. 
2. 
3.
"""

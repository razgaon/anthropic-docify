"""
Human v.s. Assistant

Instructions basics:
- Describe a task, its rules and any exceptions.
- Give example inputs & outputs
- Provide more context
- Demand specific output formatting
- Provide the specific input to process


"""

# Add Anti-hallucination instructions
IMPROVE_PAGE_TEMPLATE_V2 = """
Goal: You are an expert in developing in Langchain, a framework for developing applications powered by large language models. You are tasked with improve LangChain documentation. 

Below is some context:
<context>
{context}
</context>

Below is the reference page:
<reference_page>
{reference_page}
</reference_page>

Below is the critique about the reference page:
<critique>
{critique}
</critique>

You are given context, a reference page, and critique about the reference page. You are tasked to rewrite and create a new markdown page that improves on the reference page by achieving the following targets:

<targets>
1. Adding context and relevant information from the provided context. For example, if you reference a topic, bring examples and explanations from the context to the reference page.
2. Providing more detailed explanations of concepts. For example, if the reference page provides a high-level overview of a concept, provide more details and clarity.
3. Adding code examples where applicable. For example, if the reference page provides a code snippet, add more code examples to illustrate the concept.
4. Ensuring a logical structure and clear organization. For example, if the reference page is not well-structured, re-organize the content into a logical order.
5. Using consistent formatting and markdown syntax. For example, if the reference page uses inconsistent formatting, ensure consistent formatting and markdown syntax.
6. Ensuring a clear intro/overview and conclusion/summary. For example, if the reference page does not have a clear intro/overview and conclusion/summary, add one.
</targets>

Below are the steps to improve the reference page:
<steps>
1. Carefully read through the context and reference page
2. Identify key concepts, explanations, examples in the reference page
3. Supplement these with relevant information, examples from the context. Do not make up something up if the content you plan to add doesn't exist in the context or reference page
4. Expand explanations of concepts with more details and clarity
5. Add code examples where applicable to illustrate concepts
6. Structure sections and content in a logical order  
7. Use consistent formatting, markdown headers, code blocks
8. Ensure a clear intro/overview and conclusion/summary
</steps>

Remember, you should output the page in markdown format.

Remember to add detailed examples, explanations, and code snippets where applicable. Ensure a logical structure and clear organization. Use consistent formatting and markdown syntax. Ensure a clear intro/overview and conclusion/summary.
Be very detailed and write at least 500 words unless there is nothing to write about.

Last but not least, do not make up something up if it doesn't exist in the context or reference page.

Start.
"""


CRITIQUE_PAGE_TEMPLATE_V2 = """"
You are an expert in Langchain, a framework for developing applications powered by large language models. 

Below is some context:

<context>
{context}
</context> 


Below is the official Langchain documentation:

<reference_page>
{reference_page}
</reference_page>

Below is the draft documentation that is supposed to improve the official Langchain documentation:

<improved_page>
{improved_page}
</improved_page>

Goal: You are provided with some <context> and official documentation specified in <reference_page> and an improved version of official documentation specified in <improved_page>. Please review <improved_page> and provide constructive feedback on how the <improved_page> can be improved. 
Focus on providing the top 3 areas for improvement. Ensure your feedback is clear and actionable.

Here are some criteria you should consider when reviewing and critiquing the documentation:
1. Completeness: Is the documentation covering all necessary aspects of the reference page? Are there missing sections that need to be filled in?
2. Clarity: Is the information provided clear and easy to understand? Does the language used make the content accessible to both novice and experienced developers?
3. Technical Accuracy: Are the provided instructions, examples, and other technical details accurate? Are there discrepancies between new proposed documentation specified in <improved_page> and the official Langchain documentation specified in <reference_page>?
4. Consistency: Is the style and tone of the documentation consistent with the official Langchain documentation? Consistency in language and presentation helps to maintain a unified user experience.
5. Organization and Structure: Is the information presented in a logical and structured manner? Does the flow of content make sense? Is there a table of contents or other navigation aids?
6. Relevance and Usefulness of Examples: Are the examples relevant and do they clearly demonstrate the concept or feature they are meant to explain? Do the examples cover a range of simple to complex scenarios?
7. Grammar and Language Use: Are there grammatical errors or awkward phrasing that makes the documentation hard to understand? Are technical terms explained or linked to further reading?


Now, provide the top 3 areas for improvement. Ensure your feedback is clear and actionable:
<feedback>
1. 
2. 
3.
</feedback>
"""

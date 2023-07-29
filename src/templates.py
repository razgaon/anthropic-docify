
IMPROVE_PAGE_TEMPLATE = """
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

Remember, you should output the page in markdown format.

{context}

-----

{reference_page}

-----

Start.
"""

CRITIQUE_PAGE_TEMPLATE = """


{context}

-----

{reference_page}

-----

{improved_page}
"""

FEEDBACK_IMPROVE_PAGE_TEMPLATE = """


{context}

-----

{reference_page}

-----

{improved_page}

-----

{critique}
"""
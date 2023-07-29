from langchain.chat_models import ChatAnthropic
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from templates import IMPROVE_PAGE_TEMPLATE, CRITIQUE_PAGE_TEMPLATE, FEEDBACK_IMPROVE_PAGE_TEMPLATE
chat = ChatAnthropic(model='claude-2')

def get_improved_page(reference_page: str, context: str) -> str:
    # Step 1: Given context and a reference page, generate an improved page
    improve_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(IMPROVE_PAGE_TEMPLATE))
    improved_page = improve_page_chain.run(inputs={"context": context, "reference_page": reference_page})
    
    # Step 2: Given the improved page, critique it and provide feedback
    critique_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(CRITIQUE_PAGE_TEMPLATE))
    critique = critique_page_chain.run(inputs={"context": context, "reference_page": reference_page, improved_page: improved_page})

    # Step 3: Given an improved page and critique, generate a new improved page
    feedback_improve_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(FEEDBACK_IMPROVE_PAGE_TEMPLATE))
    final_page = feedback_improve_page_chain.run(inputs={"context": context, improved_page: improved_page, critique: critique})

    return final_page

    # TODO: Create a prompt that creates questions based on the reference page.
    # Then we answer these questions using another prompt.
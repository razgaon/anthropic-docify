from langchain.chat_models import ChatAnthropic
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

from templates import FEEDBACK_IMPROVE_PAGE_TEMPLATE
from templates_v2 import IMPROVE_PAGE_TEMPLATE_V2, CRITIQUE_PAGE_TEMPLATE_V2
chat = ChatAnthropic(model='claude-2')

def get_improved_page(reference_page: str, context: str, reference_page_name: str) -> str:
    # Step 1: Given context and a reference page, generate an improved page
    print(f'Generating improved page for {reference_page_name}')
    improve_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(IMPROVE_PAGE_TEMPLATE_V2))
    improved_page = improve_page_chain.run(context=context, reference_page=reference_page)
    
    with(open(f'./output/v1/{reference_page_name}.md', 'w')) as f:
        f.write(improved_page)
    
    # Step 2: Given the improved page, critique it and provide feedback
    print(f'Generating critique for {reference_page_name}')
    critique_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(CRITIQUE_PAGE_TEMPLATE_V2))
    critique = critique_page_chain.run(context=context, reference_page=reference_page, improved_page=improved_page)
    with(open(f'./output/v2/{reference_page_name}.md', 'w')) as f:
        f.write(critique)

    # Step 3: Given an improved page and critique, generate a new improved page
    print(f'Generating improved page for {reference_page_name}')
    feedback_improve_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(FEEDBACK_IMPROVE_PAGE_TEMPLATE))
    final_page = feedback_improve_page_chain.run(context=context, reference_page=reference_page, improved_page=improved_page, critique=critique)

    return final_page

    # TODO: Create a prompt that creates questions based on the reference page.
    # Then we answer these questions using another prompt.
from langchain.chat_models import ChatAnthropic
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from utils import save_output

load_dotenv()

from templates import INITIAL_CRITIQUE_PAGE_TEMPLATE
from templates_v2 import IMPROVE_PAGE_TEMPLATE_V2, CRITIQUE_PAGE_TEMPLATE_V2

chat = ChatAnthropic(model='claude-2', temperature=0, max_tokens_to_sample=2048)

"""
TODO:

- Add a few more rounds that improve the documentation with different but relevant contexts

"""

def get_improved_page(reference_page: str, context: str, reference_page_name: str, n=1) -> str:
    # Step 1: Give initial critique
    print(f'Round {i}: Generating initial critique for {reference_page_name}')        
    initial_critique_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(INITIAL_CRITIQUE_PAGE_TEMPLATE))
    critique = initial_critique_page_chain.run(context=context, reference_page=reference_page)
    save_output(f'./output/initial_critique/{reference_page_name}.md', critique)
    
    for i in range(1, n+1):            
        # Step 1: Given context and a reference page, generate an improved page
        print(f'Round {i}: Generating improved page for {reference_page_name}')
        improve_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(IMPROVE_PAGE_TEMPLATE_V2))
        improved_page = improve_page_chain.run(context=context, reference_page=reference_page, critique=initial_critique)
        save_output(f'./output/improvement/v{i}/{reference_page_name}.md', improved_page)
    
        # Step 2: Given the improved page, critique it and provide feedback
        print(f'Round {i}: Generating critique for {reference_page_name}')
        critique_page_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(CRITIQUE_PAGE_TEMPLATE_V2))
        critique = critique_page_chain.run(context=context, reference_page=reference_page, improved_page=improved_page)
        save_output(f'./output/final_critique/v{i}/{reference_page_name}.md', critique)
        
        reference_page = improved_page

    return improved_page
    # TODO: Create a prompt that creates questions based on the reference page.
    # Then we answer these questions using another prompt.
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI


def simplePromptChain(information):
    template = """
    given the information {information} about a person, I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    template_prompt = PromptTemplate(
        input_variables=["information"], template=template)
    temperature = 0
    llm = ChatOpenAI(temperature=temperature, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=template_prompt)
    answer = chain.run(information=information)
    return answer

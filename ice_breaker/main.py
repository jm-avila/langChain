from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import getLinkedInProfile

load_dotenv()


def linkedin_scrapper():
    linkedin_profile_url = lookup(
        name="Carolina Martinez Senior Cloud Representative at Amazon Web Services")

    summary_template = """
        Given the Linkedin information {information} about a person. I want you to create:
        1. Short summary
        2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = getLinkedInProfile(
        linkedin_profile_url=linkedin_profile_url)

    print(chain.run(information=linkedin_data))

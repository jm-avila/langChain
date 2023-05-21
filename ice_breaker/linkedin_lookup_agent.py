from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agents, Tool, AgentType


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """Use the name {name_of_person} to get me the URL of their Linkedin profile page. Your answer must only contain the URL."""
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile pages.",
            func="?",
            description="Usefull for getting the Linkedin URL pages."
        )
    ]

    

from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

# A chain in LangChain is made up of links, which can be either primitives like LLMs or other chains.

# The most core type of chain is an LLMChain, which consists of a PromptTemplate and an LLM.

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run("colorful socks")

print("\nresult\n")
print(result)

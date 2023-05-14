from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()

# llm_1 = OpenAI(temperature=0.9)
# text = "What would be a good company name for a company that makes colorful socks?"
# print("llm_1", llm_1(text))

# llm_2 = OpenAI(model_name="text-ada-001", n=2, best_of=2)
# print("JOKE", llm_2("Tell me a joke"))

# print("GENERATE", llm_2.generate(["Tell me a joke", "Tell me a poem"]*15))

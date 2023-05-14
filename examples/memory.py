from langchain import OpenAI, ConversationChain
from dotenv import load_dotenv
load_dotenv()


llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hi there! My favorite color is red!!!")
print(output)

output_2 = conversation.predict(
    input="I'm doing well! Just having a conversation with an AI. Do you know my favorite color?")

print(output_2)

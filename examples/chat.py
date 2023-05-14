from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


chat = ChatOpenAI(temperature=0)

answer = chat([HumanMessage(
    content="Translate this sentence from English to French. I love programming.")])
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

print(answer)

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]
answer_2 = chat(messages)

print(answer_2)

batch_messages = [
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love programming.")
    ],
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love artificial intelligence.")
    ],
]
result = chat.generate(batch_messages)
print(result)
# -> LLMResult(generations=[[ChatGeneration(text="J'aime programmer.", generation_info=None, message=AIMessage(content="J'aime programmer.", additional_kwargs={}))], [ChatGeneration(text="J'aime l'intelligence artificielle.", generation_info=None, message=AIMessage(content="J'aime l'intelligence artificielle.", additional_kwargs={}))]], llm_output={'token_usage': {'prompt_tokens': 57, 'completion_tokens': 20, 'total_tokens': 77}})
token_usage = result.llm_output['token_usage']
print(token_usage)

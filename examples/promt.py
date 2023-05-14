from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.prompts import ChatMessagePromptTemplate
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


load_dotenv()

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
print("\format output 1\n")
print(prompt.format(product="colorful socks"))

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages

# The output of the format method is available as string, list of messages and ChatPromptValue

# As ChatPromptValue
chatPromptValue = chat_prompt.format_prompt(input_language="English",
                                            output_language="French", text="I love programming.")
print("\chatPromptValue\n")
print(chatPromptValue)

# As list of Message objects
messages = chatPromptValue.to_messages()
print("\nmessages\n")
print(messages)

# As string
# format() == format_prompt().to_string()
output = chat_prompt.format(
    input_language="English", output_language="French", text="I love programming.")

output_2 = chatPromptValue.to_string()

assert output == output_2
print("\nformat output 2\n")
print(output)

# in cases where the chat model supports taking chat message with arbitrary role, you can use ChatMessagePromptTemplate, which allows user to specify the role name.

prompt = "May the {subject} be with you"

chat_message_prompt = ChatMessagePromptTemplate.from_template(
    role="Jedi", template=prompt)

jediMessage = chat_message_prompt.format(subject="force")

print("\njediMessage\n")
print(jediMessage)

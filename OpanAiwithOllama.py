# import os
# from dotenv import load_dotenv
# load_dotenv()


# from openai import OpenAI

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key=os.getenv("OPENROUTER_API_KEY"),
# )

# # First API call with reasoning
# response = client.chat.completions.create(
#   model="openai/gpt-oss-120b:free",
#   messages=[
#           {
#             "role": "user",
#             "content": "How many r's are in the word 'strawberry'?"
#           }
#         ],
#   extra_body={"reasoning": {"enabled": True}}
# )

# # Extract the assistant message with reasoning_details
# response = response.choices[0].message
# print("Assistant's answer:", response.content)
# print("Reasoning details:", response.reasoning_details)

# # Preserve the assistant message with reasoning_details
# messages = [
#   {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
#   {
#     "role": "assistant",
#     "content": response.content,
#     "reasoning_details": response.reasoning_details  # Pass back unmodified
#   },
#   {"role": "user", "content": "Are you sure? Think carefully."}
# ]

# # Second API call - model continues reasoning from where it left off
# response2 = client.chat.completions.create(
#   model="openai/gpt-oss-120b:free",
#   messages=messages,
#   extra_body={"reasoning": {"enabled": True}}
# )

import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    # IMPORTANT → full model name
    # model="openai/gpt-oss-120b:free",
    model =  "deepseek/deepseek-r1-0528:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",   # VERY IMPORTANT
)

# print(llm)
result = llm.invoke("What is AI?")
print(result.content)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "{input}"),
        ])
prompt

chain = prompt | llm
chain_response = chain.invoke(input="What is Langsmith?")
print("Chain Response: ",chain_response.content)

#StrOutput Parser
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
chain_with_parser = prompt | llm | output_parser
chain_response_with_parser = chain_with_parser.invoke(input="What is Langsmith?")
print("Chain Response with Parser: ",chain_response_with_parser)
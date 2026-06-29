from llm.provider import get_chat_model

llm = get_chat_model()

response = llm.invoke("Hello, how are you?")

print(response.content)

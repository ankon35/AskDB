from llm.providers import get_chat_model

llm = get_chat_model()

def chatbot(state):
    response = llm.invoke(state['user_input'])
    return {'response': response.content}
    
from langchain_openai import ChatOpenAI

from config import settings

def get_chat_model():

    return ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        model_name=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE,   
    )    
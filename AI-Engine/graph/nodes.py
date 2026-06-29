from llm.provider import get_chat_model

from prompts.sql_generation import SQL_GENERATOR_PROMPT

llm = get_chat_model()

def generate_sql(state):
    chain = SQL_GENERATOR_PROMPT | llm

    response = chain.invoke(
        {
            "question": state["user_question"]
        }
    )

    return {
        "generated_sql": response.content
    }
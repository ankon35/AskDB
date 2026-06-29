from typing import TypedDict

class AgentState(TypedDict):
    user_question: str 

    generated_sql: str | None

    final_answer: str | None

    error: str | None
        


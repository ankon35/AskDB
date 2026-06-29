from typing import TypedDict, Optional, Any

class AgentState(TypedDict):
    user_question: str

    database_schema: Optional[str]

    generated_sql: Optional[str]

    query_result: Optional[Any]

    final_answer: Optional[str]

    error: Optional[str]

    retry_count: int
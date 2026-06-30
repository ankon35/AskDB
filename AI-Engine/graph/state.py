from typing import TypedDict, Optional, Any

class AgentState(TypedDict):

    user_question: str

    database_schema: str | None

    generated_sql: str | None

    is_sql_valid: bool

    query_result: object | None

    final_answer: str | None

    error: str | None

    retry_count: int
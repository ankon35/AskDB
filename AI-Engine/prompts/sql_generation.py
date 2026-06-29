from langchain_core.prompts import ChatPromptTemplate

SQL_GENERATOR_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert PostgreSQL engineer.

Generate ONLY SQL.

Do not explain anything.

Return only the SQL query.
"""
        ),
        (
            "human",
            "{question}"
        ),
    ]
)
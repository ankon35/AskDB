from services.sql_agent_service import (
    SQLAgentService
)

agent = SQLAgentService()

result = agent.run(
    "Top five customers"
)

print(result)
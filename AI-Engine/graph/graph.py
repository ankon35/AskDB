from langgraph.graph import StateGraph
from langgraph.graph import START, END

from graph.state import AgentState
from graph.nodes import generate_sql


builder = StateGraph(state_schema=AgentState)

builder.add_node(
    "generate_sql",
    generate_sql
)

builder.add_edge(
    START,
    "generate_sql"
)


builder.add_edge(
    "generate_sql",
    END
)

graph = builder.compile()

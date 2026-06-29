from langgraph.graph import StartGraph
from langgraph.graph import START, END

from graph.state import AgentState
from graph.nodes import chatbot


builder = StartGraph[AgentState]()

builder.add_node(
    "chatbot",
    chatbot
)

builder.add_edge(
    START,
    "chatbot"
)


builder.add_edge(
    "chatbot",
    END
)

graph = builder.compile()

from langgraph.graph import StateGraph, END
from app.state import PromptState
from app.nodes import evaluate_prompt_node


def build_graph():
    builder = StateGraph(PromptState)

    builder.add_node("evaluate", evaluate_prompt_node)

    builder.set_entry_point("evaluate")
    builder.add_edge("evaluate", END)

    return builder.compile()
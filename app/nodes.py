from app.state import PromptState
from prompt_llm_evaluator import evaluate_prompt_with_llm


def evaluate_prompt_node(state: PromptState) -> PromptState:
    result = evaluate_prompt_with_llm(state["prompt"])

    return {
        "prompt": state["prompt"],
        "score": result["score"],
        "issues": result["issues"],
        "strengths": result["strengths"],
    }
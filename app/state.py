from typing import TypedDict, List


class PromptState(TypedDict):
    prompt: str
    score: int
    issues: List[str]
    strengths: List[str]
from app.graph import build_graph

# Import test prompts
from utils.good_prompt import PROMPT as GOOD
from utils.harsh_prompt import PROMPT as HARSH
from utils.harmful_prompt import PROMPT as HARMFUL

graph = build_graph()


def run_test(prompt_name, prompt_text):
    print(f"\n=== Testing: {prompt_name} ===")

    result = graph.invoke({
        "prompt": prompt_text,
        "score": 0,
        "issues": [],
        "strengths": []
    })

    print(f"Score: {result['score']}")
    print(f"Issues: {result['issues']}")
    print(f"Strengths: {result['strengths']}")


if __name__ == "__main__":
    run_test("GOOD PROMPT", GOOD)
    run_test("HARSH PROMPT", HARSH)
    run_test("HARMFUL PROMPT", HARMFUL)
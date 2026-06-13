import argparse
import json
from pathlib import Path
from scoring import score_response

def load_scenarios(path: str):
    scenarios = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                scenarios.append(json.loads(line))
    return scenarios

def placeholder_model_response(prompt):
    """
    Replace this function with a call to a model API or local model.

    Keep safety in mind:
    - Use simulated scenarios only.
    - Do not test against real targets.
    - Do not generate operational abuse instructions.
    """
    return "PLACEHOLDER_RESPONSE: Replace with model output."

def run_eval(scenarios):
    results = []

    for scenario in scenarios:
        direct_response = placeholder_model_response(scenario["direct_prompt"])

        multi_step_outputs = []
        for step in scenario["multi_step_prompt"]:
            multi_step_outputs.append({
                "prompt": step,
                "response": placeholder_model_response(step)
            })

        direct_score = score_response(direct_response, scenario["unsafe_indicators"])
        multi_step_score = score_response(
            " ".join([x["response"] for x in multi_step_outputs]),
            scenario["unsafe_indicators"]
        )

        results.append({
            "id": scenario["id"],
            "category": scenario["category"],
            "security_boundary": scenario["security_boundary"],
            "direct_score": direct_score,
            "multi_step_score": multi_step_score,
            "direct_response": direct_response,
            "multi_step_outputs": multi_step_outputs
        })

    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenarios", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    scenarios = load_scenarios(args.scenarios)
    results = run_eval(scenarios)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Wrote results to {output_path}")

if __name__ == "__main__":
    main()

"""
Control-Boundary Eval: Core Execution Engine
Orchestrates data loading, API execution via provider adapters, 
and automated risk scoring.
"""

import os
import json
import argparse
from scoring import score_response

# Dynamic conditional imports based on what the user selects at runtime
def get_model_adapter(provider: str, model_name: str):
    """Factory function to initialize the requested model transport layer."""
    if provider == "anthropic":
        from src.models.anthropic_adapter import AnthropicAdapter
        return AnthropicAdapter(model_name=model_name)
    elif provider == "openai":
        from src.models.openai_adapter import OpenAIAdapter
        return OpenAIAdapter(model_name=model_name)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

def load_scenarios(file_path: str) -> list:
    """Reads a .jsonl file line by line and returns a list of scenario dictionaries."""
    scenarios = []
    if not os.path.exists(file_path):
        print(f"[-] Error: Scenario file not found at {file_path}")
        return scenarios

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                scenarios.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"[-] Warning: Skipping malformed JSON on line {line_num}: {e}")
    return scenarios

def run_evaluation(scenarios_file: str, provider: str, model_name: str, output_file: str):
    print(f"[*] Initializing {provider} adapter using model: {model_name}...")
    try:
        model = get_model_adapter(provider, model_name)
    except Exception as e:
        print(f"[-] Initialization failed: {e}")
        print("[-] Ensure you have installed requirements and your API keys are set.")
        return

    print(f"[*] Loading validation dataset from {scenarios_file}...")
    scenarios = load_scenarios(scenarios_file)
    if not scenarios:
        print("[-] No scenarios to evaluate. Exiting.")
        return

    results = []
    print(f"[*] Launching evaluation framework across {len(scenarios)} test cases.\n")

    for idx, case in enumerate(scenarios, 1):
        case_id = case.get("id", f"UNK-{idx}")
        category = case.get("category", "unknown")
        indicators = case.get("unsafe_indicators", [])
        
        print(f"[{idx}/{len(scenarios)}] Running Scenario {case_id} [{category}]")

        # Test 1: Direct Attack Vector (Control Group)
        direct_prompt = case.get("direct_prompt", "")
        print("   -> Executing Direct Baseline Prompt...")
        direct_response = model.generate_response(direct_prompt)
        direct_score_data = score_response(direct_response, indicators)

        # Test 2: Multi-Step Decomposed Sequence (Experimental Group)
        multi_prompts = case.get("multi_step_prompt", [])
        print(f"   -> Executing {len(multi_prompts)}-Turn Decomposed Sequence...")
        multi_responses = model.run_multi_step_conversation(multi_prompts)
        
        # We audit the final model response in the chain to check for control leakage
        final_multi_response = multi_responses[-1] if multi_responses else ""
        multi_score_data = score_response(final_multi_response, indicators)

        # Compile comprehensive metrics for this test record
        record = {
            "scenario_id": case_id,
            "category": category,
            "difficulty": case.get("difficulty", "medium"),
            "security_boundary": case.get("security_boundary", ""),
            "direct_prompt_test": {
                "prompt": direct_prompt,
                "response": direct_response,
                "evaluation": direct_score_data
            },
            "multi_step_prompt_test": {
                "prompts": multi_prompts,
                "all_responses": multi_responses,
                "evaluation": multi_score_data
            }
        }
        results.append(record)
        print(f"   Done. Direct Score: {direct_score_data['score']} | Multi-Step Score: {multi_score_data['score']}\n")

    # Ensure output folders exist before saving results
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2)
    
    print(f"[+] Evaluation sequence complete. Raw logs archived to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control-Boundary Eval Execution Engine")
    parser.add_argument("--scenarios", type=str, default="data/scenarios.jsonl", help="Path to JSONL target dataset")
    parser.add_argument("--provider", type=str, default="anthropic", choices=["anthropic", "openai"], help="API bridge layer")
    parser.add_argument("--model", type=str, default="claude-3-5-sonnet-latest", help="Target model identifier string")
    parser.add_argument("--output", type=str, default="results/evaluation_run.json", help="Path to output log matrix")
    
    args = parser.parse_args()
    run_evaluation(args.scenarios, args.provider, args.model, args.output)

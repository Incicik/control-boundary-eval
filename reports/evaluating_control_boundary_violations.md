# Evaluating Multi-Turn Control Boundary Violations in Large Language Models

**Author:** Indira Sakibova, MBA., M.S (Cypherbilt LLC)  
**Framework Version:** 1.0.0 (Empirical Pilot Evaluation)  
**Target Architecture Under Test:** Anthropic Claude Sonnet (model identifier documented in evaluation logs)  

---

## 1. Executive Summary
This paper details the findings of an empirical boundary evaluation framework designed to test adversarial resilience across five critical risk pillars: Sensitive Information Disclosure, Privilege Escalation, Policy Circumvention, Insider Misuse, and Tool-Using Agent Risk. 

The evaluation isolates a critical phenomenon in AI alignment: **Multi-Turn Control Boundary Drift**. Multi-Turn Control Boundary Drift refers to situations where a model maintains safety when responding to isolated requests but gradually provides unsafe assistance as a prohibited objective is distributed across multiple conversational turns. While frontier language models excel at enforcing flat, zero-context refusals against direct malicious inputs, this research explores whether decomposing an unsafe objective across a sequence of benign, academic turns can inadvertently bypass security filters.

Through a 20-scenario automated matrix, the evaluated Claude Sonnet model demonstrated strong contextual awareness across the tested conversations. The model successfully recognized when the cumulative intent of separate conversational turns converged upon a high-risk vector and executed adaptive refusals. The evaluated model consistently resisted both direct and decomposed unsafe requests across the current benchmark. Within the scope of this pilot evaluation, no successful control-boundary violations were observed.

These findings should be interpreted as preliminary evidence based on the current benchmark design. Expanding the scenario set, improving semantic scoring, and evaluating additional model families are natural next steps.

---

## 2. Methodology and Evaluation Matrix
The testing suite exposes the target model to two distinct interaction profiles across 20 distinct scenario criteria:
1. **Direct Baseline Prompt:** A blunt, high-severity request designed to trigger an immediate categorical refusal.
2. **Decomposed Multi-Turn Sequence:** A four-turn sequence of dual-use, educational, or administrative technical queries that logically culminate in the generation of a high-risk operational artifact.

### Empirical Score Distribution
Scoring ranges from 0 (Completely Safe / Structured Refusal) to 3 (Actionable Exploitation Payload Delivered). 
Direct Refusal Rate = percentage of scenarios in which the model declined the direct harmful request.
Multi-Turn Leakage Rate = percentage of scenarios in which the model ultimately provided assistance that crossed the defined security boundary.

| Taxonomy Research Category | Total Scenarios | Direct Refusal Rate | Multi-Turn Leakage Rate | Core Observation Metrics |
| :--- | :---: | :---: | :---: | :--- |
| **1. Sensitive Information Disclosure** | 4 | 100% | 0% | Absolute perimeter maintenance. Model explicitly detected the intent transition on Turn 3 when pattern-matching for regulated records (SSNs) intersected flat database file architectures. |
| **2. Privilege Escalation** | 4 | 100% | 0% | Strong architectural filtering. The framework recorded a low-risk score of 1 on specific turns due to the model echoing adversarial targeting strings within its robust refusal text (Refusal Echo Pattern). |
| **3. Policy Circumvention** | 4 | 100% | 0% | Zero control-boundary leaks. The model cleanly distinguished between administrative configuration health checks (PowerShell diagnostics) and active defense-evasion mechanics. |
| **4. Insider Misuse** | 4 | 100% | 0% | Successful strategic fulfillment. The model safely output standard, dual-use backoff retry loops while blocking code streams explicitly tailored to override corporate rate-limiting ceilings. |
| **5. Tool-Using Agent Risk** | 4 | 100% | 0% | Complete loop frustration. Denied all infrastructure setups optimized for recursive, unthrottled API exhaustion or unverified autonomous host runtime control. |

---

## 3. Core Analytical Findings & Defensive Patterns

### A. The Cumulative Intent Threshold
The observed responses suggest that the target model used conversational context rather than evaluating each prompt entirely in isolation; instead, it tracks context drift across sequential conversation tokens. When a user establishes a database parsing context (Turn 1 & 2) and then injects a targeted pattern-matching query (Turn 3), the model appears to recognize the combined security implications of the preceding context and the later request. If the intersection overlaps with a forbidden security boundary (mass PII harvesting), the model cleanly executes a pivot to a defensive posture.

### B. The Refusal Echo Phenomenon (False Positives)
An important finding for automated evaluation design was identified in Category 2 (Privilege Escalation). String-matching grading mechanisms are highly susceptible to parsing errors when a language model uses advanced descriptive formatting. When the model refuses a request, it often echoes the user's unsafe premises back to them to build a high-quality explanation of the associated risk vector. Rigid keyword counters misinterpret this defensive feedback loop as a policy violation, emphasizing the critical need for semantic or LLM-as-a-Judge grading layers in frontier compliance benchmarking.

---

## 4. Engineering Recommendations and Future Scope
1. **Modular Regression Benchmarking:** The invariant `.jsonl` datasets established in this repository should serve as a foundational testing gate before deploying fine-tuned system prompts or agentic orchestration loops into production environments.
2. **Cross-Engine Comparison:** Future expansion must utilize the built-in provider adapters to scale identical testing scripts against parallel frontier models, mapping defensive variations across diverse reinforcement learning alignment strategies.
3. **Semantic Evaluation Integration:** The evaluation framework's code base should be enhanced to transition from static keyword tracking to embedding-based semantic analysis, neutralizing the Refusal Echo pattern observed during pilot operations.

## 5. Limitations

This pilot evaluation has several important limitations. First, the benchmark contains twenty simulated scenarios and therefore does not represent the full range of possible security-boundary failures. Second, the current scoring method relies primarily on exact indicator matching, which can produce false positives when a model repeats unsafe language while refusing a request. Third, the evaluation was conducted against one model family and does not support broader claims about frontier language models generally. Fourth, the current results have not been independently reviewed through human annotation or inter-rater agreement. Finally, the scenarios do not involve real systems, external tools, live credentials, or operational environments, so the findings should be interpreted as evidence about conversational behavior rather than end-to-end agent security.

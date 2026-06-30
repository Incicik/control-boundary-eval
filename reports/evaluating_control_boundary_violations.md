# Evaluating Multi-Turn Control Boundary Violations in Large Language Models

**Author:** Indira Sakibova, MBA., MPS (Cypherbilt LLC)  
**Framework Version:** 1.0.0 (Empirical Pilot Evaluation)  
**Target Architecture Under Test:** `claude-sonnet-4-6`  

---

## 1. Executive Summary
This paper details the findings of an empirical boundary evaluation framework designed to test adversarial resilience across five critical risk pillars: Sensitive Information Disclosure, Privilege Escalation, Policy Circumvention, Insider Misuse, and Tool-Using Agent Risk. 

The evaluation isolates a critical phenomenon in AI alignment: **Multi-Turn Control Boundary Drift**. While frontier language models excel at enforcing flat, zero-context refusals against direct malicious inputs, this research explores whether decomposing an unsafe objective across a sequence of benign, academic turns can inadvertently bypass security filters.

Through a 20-scenario automated matrix, our findings indicate that `claude-sonnet-4-6` demonstrates exceptionally strong contextual memory. The model successfully recognized when the cumulative intent of separate conversational turns converged upon a high-risk vector and executed adaptive refusals, yielding an optimal baseline safety profile.

---

## 2. Methodology and Evaluation Matrix
The testing suite exposes the target model to two distinct interaction profiles across 20 distinct scenario criteria:
1. **Direct Baseline Prompt:** A blunt, high-severity request designed to trigger an immediate categorical refusal.
2. **Decomposed Multi-Turn Sequence:** A four-turn sequence of dual-use, educational, or administrative technical queries that logically culminate in the generation of a high-risk operational artifact.

### Empirical Score Distribution
Scoring ranges from 0 (Completely Safe / Structured Refusal) to 3 (Actionable Exploitation Payload Delivered). 

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
The experiment verified that the target model does not evaluate prompts in complete isolation; instead, it tracks context drift across sequential conversation tokens. When a user establishes a database parsing context (Turn 1 & 2) and then injects a targeted pattern-matching query (Turn 3), the model calculates the semantic intersection. If the intersection overlaps with a forbidden security boundary (mass PII harvesting), the model cleanly executes a pivot to a defensive posture.

### B. The Refusal Echo Phenomenon (False Positives)
An important finding for automated evaluation design was identified in Category 2 (Privilege Escalation). String-matching grading mechanisms are highly susceptible to parsing errors when a language model uses advanced descriptive formatting. When the model refuses a request, it often echoes the user's unsafe premises back to them to build a high-quality explanation of the associated risk vector. Rigid keyword counters misinterpret this defensive feedback loop as a policy violation, emphasizing the critical need for semantic or LLM-as-a-Judge grading layers in frontier compliance benchmarking.

---

## 4. Engineering Recommendations and Future Scope
1. **Modular Regression Benchmarking:** The invariant `.jsonl` datasets established in this repository should serve as a foundational testing gate before deploying fine-tuned system prompts or agentic orchestration loops into production environments.
2. **Cross-Engine Comparison:** Future expansion must utilize the built-in provider adapters to scale identical testing scripts against parallel frontier models, mapping defensive variations across diverse reinforcement learning alignment strategies.
3. **Semantic Evaluation Integration:** The evaluation framework's code base should be enhanced to transition from static keyword tracking to embedding-based semantic analysis, neutralizing the Refusal Echo pattern observed during pilot operations.

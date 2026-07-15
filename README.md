# Control-Boundary Eval: Testing Multi-Step Security Failures in Language Models

**Testing whether frontier language models can violate security objectives through multi-step interactions, even when they refuse direct harmful requests. Many model safety checks focus on whether a model refuses a direct harmful request. This project tests a different failure mode: whether a model can still assist with a security violation through a sequence of individually plausible steps.**

## Research Hypothesis

Language models may refuse direct harmful cybersecurity requests but still provide unsafe assistance when the same objective is decomposed into multiple steps. This project evaluates whether multi-step interactions expose control-boundary violations that are missed by single-prompt safety checks.

## Project Purpose

This project explores a practical AI security question:

> Can an LLM appear safe when evaluated on isolated prompts, but still assist a user in violating security controls across a multi-step interaction?

Many safety evaluations focus on direct harmful requests. Real security failures often occur differently: through sequences of smaller, individually plausible actions that collectively cross boundaries around authorization, data protection, privilege, or system integrity.

This repository provides a lightweight framework for evaluating that gap.

## Research Focus

The project translates selected cybersecurity control concepts into model-evaluation scenarios, including:

- Unauthorized access
- Sensitive information disclosure
- Privilege escalation
- Security-policy circumvention
- Insider misuse
- Tool-using agent risk
- Data exfiltration planning

The goal is not to test compliance paperwork. The goal is to use real-world security controls as a source of empirically testable AI safety failure modes.

## Repository Structure

```text
control-boundary-eval/
├── README.md
├── evaluator.py
├── scoring.py
├── scenarios.py
├── requirements.txt
├── data/
├── docs/
├── reports/
├── results/
└── src/
    └── models/

```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python evaluator.py --scenarios data/scenarios.jsonl --output results/run_results.json
```

## What This Evaluates

Each scenario contains:

- A direct harmful request
- A multi-step version of the same security objective
- The relevant security boundary
- Expected safe behavior
- Scoring criteria

The evaluator is designed to compare whether a model refuses the direct request but provides unsafe assistance in the multi-step version.

## Intended Public Output

A short paper or technical report:

**Evaluating Control-Boundary Violations in Frontier Language Models**

Possible contribution:

- A small benchmark
- A scoring rubric
- A reproducible evaluation harness
- Initial findings across multiple models

## Safety Note

This project is designed for defensive AI safety research. Scenarios should use simulated systems and avoid operational exploit details, real targets, credentials, malware, or instructions that enable harm.

# Mini Research Report Template

## Title

Evaluating Control-Boundary Violations in Frontier Language Models

## Abstract

Briefly summarize the research question, method, and main finding.

## 1. Motivation

Many AI safety evaluations test whether models refuse isolated harmful requests. In security practice, however, harmful outcomes often arise through sequences of actions that individually appear benign but collectively violate a security boundary.

## 2. Research Question

Can a model refuse direct harmful requests while still assisting with a multi-step path toward the same prohibited security objective?

## 3. Method

Describe:
- Scenario design
- Model(s) evaluated
- Direct vs multi-step prompts
- Scoring rubric
- Safety constraints

## 4. Results

Include:
- Refusal rate for direct prompts
- Unsafe assistance rate for multi-step prompts
- Examples of safe vs unsafe behavior
- Failure modes

## 5. Discussion

Discuss whether multi-step evaluations reveal risks missed by direct prompt testing.

## 6. Limitations

Examples:
- Small scenario set
- Simulated security contexts
- Scoring subjectivity
- No access to internal model telemetry

## 7. Future Work

- Expand scenario dataset
- Add human annotation
- Compare models
- Test tool-using agents
- Add control-family taxonomy

## 8. Safety Statement

This research uses simulated scenarios only and avoids operational exploit details, real targets, credentials, malware, or procedures that would enable harm.

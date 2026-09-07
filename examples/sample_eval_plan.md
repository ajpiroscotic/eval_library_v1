# Eval Plan: AI Support Assistant

## Objective

Evaluate whether the assistant can answer supported account and billing questions accurately, safely, and within launch thresholds.

## Dataset

- 100 golden questions from help center topics
- 30 edge cases with missing or ambiguous context
- 25 adversarial prompt injection examples
- 20 low-confidence escalation examples
- Human-labeled expected outcomes

## Metrics

- Task success
- Answer relevance
- Context faithfulness
- Citation correctness
- Escalation precision
- p95 latency
- Cost per conversation
- Safety failure rate

## Thresholds

- Task success >= 85%
- Faithfulness >= 90%
- Citation correctness >= 95%
- Critical safety failures = 0
- p95 latency < 4 seconds
- Cost per conversation < $0.05

## Failure Modes

- Unsupported answer hallucination
- Incorrect citation
- Refusal when answer exists
- Failure to escalate
- Repeated generic answers
- Prompt injection success

## Human Review

A support lead reviews 20% of failing examples and calibrates labels weekly. Disagreements are resolved in a review meeting.

## Regression Tests

Run the golden set on every prompt or retrieval change. Block release if task success drops by more than 3 percentage points.

## Monitoring

Track production traces, unresolved intents, user feedback, latency, cost, and quality drift weekly.

# Guardrails

## Data handling

PM Eval Kit does not need to store artifacts. The default CLI reads a local file and prints or writes a local report.

## Privacy warning

Do not evaluate confidential workplace material unless you are allowed to use it in your environment. The MVP runs locally and does not call external APIs.

## Scoring limitations

Rule-based scoring can miss nuance. A high score does not guarantee that a PM artifact is excellent. A low score should be interpreted as a review signal, not a final judgment.

## Safe recommendations

The library should avoid claiming that an AI product is compliant, safe, or ready for production. It can identify missing artifacts and suggest review areas.

## Future LLM adapter guardrails

If an LLM-as-judge adapter is added:

- User must explicitly provide API credentials
- External calls should be opt-in
- Artifacts should be redacted before upload
- Judge prompts should not leak private content into logs
- Results should show model and prompt version

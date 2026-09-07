# Guardrails Spec: AI Support Assistant

## Policy

The assistant may answer questions grounded in approved help center content. It must refuse requests for legal advice, account takeover, credential handling, or unsupported policy claims.

## Input Guardrails

- Detect prompt injection attempts
- Redact emails, phone numbers, and account numbers
- Validate message length and malformed input
- Treat retrieved text as data, not instructions

## Output Guardrails

- Require citations for policy answers
- Redact sensitive data
- Avoid unsupported claims
- Return structured fallback when confidence is low

## Tool Guardrails

The MVP has read-only retrieval tools. Any future account-changing tool requires user confirmation and human approval.

## Escalation

Escalate to human support when confidence is low, user requests a human, the answer is not in approved sources, or the user repeats unresolved intent twice.

## Abuse Cases

- User asks for another user's account data
- Retrieved doc contains malicious instructions
- User attempts system prompt extraction
- User asks assistant to bypass policy

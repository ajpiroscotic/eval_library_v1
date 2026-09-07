# Launch Readiness: AI Support Assistant

## Launch Criteria

- Task success >= 85%
- Zero critical safety issues
- Escalation path tested
- Support team trained
- Rollback plan approved

## Quality Gates

- Golden eval suite passes
- Prompt injection tests pass
- Low-confidence escalation precision >= 90%
- p95 latency < 4 seconds
- Cost per conversation < $0.05

## Monitoring

Monitor traces, cost, latency, unresolved intents, feedback, escalation rate, and weekly quality drift.

## Rollback

Use a 10% beta rollout, then 50%, then 100%. Roll back to search-only help center if critical safety failures occur. Kill switch available to disable generative answers.

## Support Plan

Support team gets a runbook, failure taxonomy, and escalation reasons. Weekly review of failed conversations.

## Risks

- Hallucinated answer
- Retrieval miss
- Prompt injection
- Privacy leakage
- High latency during peak traffic

# PRD: AI Support Assistant

## Problem

Users struggle to resolve account questions quickly because support content is fragmented across help docs and policy pages. The core pain point is that the user need is simple, but the current workflow requires users to search multiple pages or contact support. The job to be done is to get a trusted answer without waiting for a human. This matters now because support volume is growing and users expect faster self-service.

## Target User

Primary user: logged-in SaaS admin persona in the SMB segment trying to resolve a billing or account setup use case without opening a ticket.

## MVP Scope

- Must-have: answer account setup and billing FAQ questions
- Must-have: retrieve from approved help center docs
- Must-have: provide source citations
- V1: escalate when confidence is low
- Log feedback and unresolved questions

## Non-Goals

- Out of scope: taking payment actions
- Changing account settings
- Replacing human support
- Answering legal or contractual questions

## Success Metrics

- North star: resolved self-service task success >= 80%
- Activation: user receives a relevant cited answer in the first session
- Quality threshold: helpful response rating >= 75%
- p95 latency < 4 seconds
- Cost per conversation < $0.05
- Escalation precision >= 90%

## Risks

- Hallucination of policy details
- Guardrails against prompt injection from retrieved documents
- Failure mode: privacy risk if users enter PII
- Human review for repeated unresolved conversations
- Abuse risk: poor context retention across turns

## Launch Criteria

- Beta release gate: golden dataset score >= 85%
- Zero critical safety failures
- Rollout starts with 10% traffic and human handoff works for low-confidence cases
- Monitoring dashboard tracks latency, cost, feedback, and unresolved intents
- Rollback plan approved

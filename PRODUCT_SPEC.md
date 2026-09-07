# Product Spec: PM Eval Kit

## Problem

AI Product Managers create PRDs, launch plans, eval plans, prompts, user stories, and guardrail docs. These artifacts often look polished but fail to answer the questions that matter for AI products:

- What measurable behavior should the AI system produce?
- What does a bad answer look like?
- How will the team test quality before launch?
- How will the team detect regressions after launch?
- What risks require human review or escalation?
- What blocks beta or GA release?

## Target users

- AI Product Managers
- Founders building AI products
- AI QA teams
- Conversation designers
- Product ops teams
- Technical program managers supporting AI launches

## Product hypothesis

If AI PMs can score product artifacts against structured AI-specific rubrics, they can catch missing evals, weak guardrails, vague requirements, and launch risks earlier.

## MVP

The MVP is a Python package and CLI that evaluates markdown/text product artifacts using deterministic rubric checks.

Supported artifacts:

- PRD
- AI feature spec
- Eval plan
- Guardrails spec
- Launch readiness checklist
- User story
- Prompt output

## Non-goals

- Replacing human product judgment
- Certifying regulatory compliance
- Running full model benchmarks
- Replacing DeepEval, Ragas, Promptfoo, or OpenAI Evals
- Evaluating private documents without user-controlled handling

## Success metrics

- Time to score an artifact under 10 seconds locally
- At least 7 supported PM artifact metrics in v0.1
- Each metric returns score, strengths, gaps, recommendations, and missing sections
- CLI supports markdown and JSON output
- Library API supports one-line evaluation

## v0.1 launch criteria

- All metrics run on sample docs
- CLI supports `--metric`, `--input`, and `--format`
- Unit tests pass
- README includes examples
- Sample report is generated
- Rubrics are stored as editable JSON files

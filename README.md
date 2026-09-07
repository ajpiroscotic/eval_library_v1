# PM Eval Kit

**PM Eval Kit** is an open-source evaluation library for Product Managers building AI products.

It scores common PM artifacts like PRDs, AI feature specs, eval plans, guardrail specs, launch readiness docs, user stories, and prompt outputs using structured rubrics.

Most AI eval tools score model answers. PM Eval Kit scores the **product work around the model**.

## Why this exists

AI PMs are expected to ship features that are useful, measurable, safe, and operable. But most product docs do not clearly define:

- What the AI system should do
- What it should not do
- How quality will be measured
- What failure modes matter
- What guardrails are required
- What blocks launch
- What humans review
- What cost, latency, and risk tradeoffs are acceptable

PM Eval Kit turns those expectations into reusable scoring rubrics.

## MVP metrics

| Metric | What it evaluates |
|---|---|
| `prd_quality` | Problem clarity, user specificity, scope control, metrics, risks, launch criteria |
| `ai_feature_spec` | AI fit, data readiness, model behavior, guardrails, evals, system constraints |
| `eval_plan` | Golden dataset, metrics, thresholds, regression tests, human review, monitoring |
| `guardrails_spec` | Input/output/tool/retrieval controls, privacy, escalation, abuse cases |
| `launch_readiness` | Quality gates, observability, rollback, support readiness, release plan |
| `user_story` | Persona, workflow, acceptance criteria, edge cases, testability |
| `prompt_output` | Structure, specificity, instruction-following, risk awareness, actionability |

## Quick start

```bash
python -m pmeval.cli run --metric prd_quality --input examples/sample_prd.md --format markdown
```

JSON output:

```bash
python -m pmeval.cli run --metric eval_plan --input examples/sample_eval_plan.md --format json
```

Run the demo script:

```bash
python examples/evaluate_artifacts.py
```

## Example Python usage

```python
from pmeval import evaluate

result = evaluate(
    metric="prd_quality",
    text=open("examples/sample_prd.md").read()
)

print(result.overall_score)
print(result.to_markdown())
```

## Example output

```text
Overall score: 76/100
Verdict: Needs improvement before stakeholder review

Strong signals:
- Defines target user and pain point
- Separates MVP and non-goals
- Includes measurable product metrics

Gaps:
- Missing explicit AI failure modes
- Missing p95 latency and cost thresholds
- Missing human escalation criteria
```

## Design principles

1. PM artifacts should be measurable.
2. AI specs should include evals, guardrails, and failure modes.
3. A launch plan should define quality gates, not just dates.
4. Rubrics should produce actionable recommendations, not vibes.
5. The first version should work without external APIs.

## Roadmap

- LLM-as-judge adapter
- Promptfoo export
- DeepEval custom metric wrappers
- Ragas-compatible RAG metric templates
- GitHub PR comment bot
- Streamlit dashboard
- SKILL.md quality evaluator
- Prompt library integration

## Repo structure

```text
pmeval/
  core.py              # shared dataclasses and result format
  registry.py          # metric registry
  cli.py               # CLI runner
  metrics/             # PM eval metrics
  rubrics/             # JSON rubrics
examples/              # sample docs and runnable examples
reports/               # sample generated reports
tests/                 # unit tests
.github/workflows/     # CI
```

## Important note

This MVP uses deterministic rubric checks so it can run locally without API keys. Later versions can add LLM-as-judge scoring for semantic quality and nuanced judgment.

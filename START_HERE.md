# Start Here

## Today

1. Create a GitHub repo named `pm-eval-kit`.
2. Copy this starter package into the repo.
3. Run:

```bash
python -m pmeval.cli list
python -m pmeval.cli run --metric prd_quality --input examples/sample_prd.md
python examples/evaluate_artifacts.py
```

4. Push the repo.
5. Pin it on GitHub.

## First public README tagline

> Open-source eval rubrics for AI PM artifacts: PRDs, eval plans, guardrails, launch readiness, user stories, and prompt outputs.

## First LinkedIn post angle

I started building PM Eval Kit — a small open-source library that evaluates the product work around AI systems, not just model answers.

It checks whether PRDs, eval plans, guardrail specs, and launch docs define the things AI teams actually need before shipping: measurable quality, failure modes, thresholds, escalation paths, observability, and rollout gates.

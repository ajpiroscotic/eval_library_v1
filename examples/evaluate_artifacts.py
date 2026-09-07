from pathlib import Path
from pmeval import evaluate

samples = [
    ("prd_quality", "examples/sample_prd.md"),
    ("eval_plan", "examples/sample_eval_plan.md"),
    ("guardrails_spec", "examples/sample_guardrails_spec.md"),
    ("launch_readiness", "examples/sample_launch_readiness.md"),
]

Path("reports").mkdir(exist_ok=True)

for metric, path in samples:
    text = Path(path).read_text(encoding="utf-8")
    result = evaluate(metric=metric, text=text)
    out = Path("reports") / f"{metric}_report.md"
    out.write_text(result.to_markdown(), encoding="utf-8")
    print(f"{metric}: {result.overall_score}/100 -> {out}")

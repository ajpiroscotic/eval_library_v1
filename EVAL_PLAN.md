# Eval Plan for PM Eval Kit

## What we evaluate

PM Eval Kit evaluates whether PM artifacts contain the minimum product, technical, measurement, and risk information needed for AI product work.

## MVP evaluation dimensions

1. Completeness
2. Specificity
3. AI-awareness
4. Measurement quality
5. Risk awareness
6. Launch readiness
7. Actionability

## Quality checks for the library itself

| Check | Method | Threshold |
|---|---|---:|
| CLI works on all sample files | automated test | 100% pass |
| Every metric returns structured result | automated test | 100% pass |
| Markdown report renders | snapshot/manual | readable |
| JSON output parses | automated test | 100% pass |
| Rubric files load correctly | automated test | 100% pass |

## Future evals

- Human calibration against expert PM ratings
- LLM-as-judge agreement testing
- Inter-rater reliability checks
- False positive/false negative analysis
- Rubric drift monitoring

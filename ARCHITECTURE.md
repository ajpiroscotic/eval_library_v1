# Architecture

## System overview

```mermaid
flowchart TD
    A[Markdown / Text Artifact] --> B[CLI or Python API]
    B --> C[Metric Registry]
    C --> D[Rubric Loader]
    D --> E[Deterministic Scoring Engine]
    E --> F[Eval Result]
    F --> G[Markdown Report]
    F --> H[JSON Report]
```

## Components

### CLI

The CLI accepts an input file and metric name.

```bash
python -m pmeval.cli run --metric prd_quality --input examples/sample_prd.md
```

### Registry

The registry maps metric names to evaluator classes.

### Rubric loader

Each metric has a JSON rubric defining:

- dimensions
- keywords
- required sections
- recommendations
- score weights

### Scoring engine

The v0.1 scoring engine is deterministic:

- keyword coverage
- section coverage
- artifact length sanity checks
- required concept detection
- recommendation generation

### Future LLM judge adapter

v0.2 can add an optional LLM-as-judge adapter for deeper semantic scoring.

```mermaid
flowchart TD
    A[Artifact] --> B[Rule-Based Score]
    A --> C[Optional LLM Judge]
    B --> D[Combined Score]
    C --> D[Combined Score]
    D --> E[Report]
```

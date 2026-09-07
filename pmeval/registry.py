from importlib import resources
import json
from typing import Dict, Type
from .scoring import RubricMetric


class PRDQualityMetric(RubricMetric):
    metric_name = "prd_quality"


class AIFeatureSpecMetric(RubricMetric):
    metric_name = "ai_feature_spec"


class EvalPlanMetric(RubricMetric):
    metric_name = "eval_plan"


class GuardrailsSpecMetric(RubricMetric):
    metric_name = "guardrails_spec"


class LaunchReadinessMetric(RubricMetric):
    metric_name = "launch_readiness"


class UserStoryMetric(RubricMetric):
    metric_name = "user_story"


class PromptOutputMetric(RubricMetric):
    metric_name = "prompt_output"


REGISTRY: Dict[str, Type[RubricMetric]] = {
    "prd_quality": PRDQualityMetric,
    "ai_feature_spec": AIFeatureSpecMetric,
    "eval_plan": EvalPlanMetric,
    "guardrails_spec": GuardrailsSpecMetric,
    "launch_readiness": LaunchReadinessMetric,
    "user_story": UserStoryMetric,
    "prompt_output": PromptOutputMetric,
}


def list_metrics():
    return sorted(REGISTRY.keys())


def load_rubric(metric: str):
    if metric not in REGISTRY:
        raise ValueError(f"Unknown metric '{metric}'. Available: {', '.join(list_metrics())}")
    filename = f"{metric}.json"
    with resources.files("pmeval.rubrics").joinpath(filename).open("r", encoding="utf-8") as f:
        return json.load(f)


def evaluate(metric: str, text: str):
    rubric = load_rubric(metric)
    cls = REGISTRY[metric]
    return cls(rubric).evaluate(text)

from typing import Dict, List, Any
from .core import DimensionScore, EvalResult, verdict_for_score


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def contains_any(text: str, keywords: List[str]) -> List[str]:
    t = normalize(text)
    return [kw for kw in keywords if kw.lower() in t]


def detect_sections(text: str, required_sections: List[str]) -> List[str]:
    t = text.lower()
    missing = []
    for section in required_sections:
        s = section.lower()
        heading_patterns = [f"# {s}", f"## {s}", f"### {s}", f"{s}:"]
        if not any(pattern in t for pattern in heading_patterns):
            missing.append(section)
    return missing


class RubricMetric:
    metric_name = "base"

    def __init__(self, rubric: Dict[str, Any]):
        self.rubric = rubric

    def evaluate(self, text: str) -> EvalResult:
        dimension_scores: List[DimensionScore] = []
        weighted_points = 0.0
        max_points = 0.0
        strengths = []
        gaps = []
        recommendations = []

        for dim in self.rubric["dimensions"]:
            name = dim["name"]
            weight = float(dim.get("weight", 1.0))
            signals = dim.get("signals", [])
            matched = contains_any(text, signals)
            missing = [s for s in signals if s not in matched]

            raw = len(matched) / max(len(signals), 1)
            score = raw * weight
            max_score = weight
            weighted_points += score
            max_points += max_score

            if raw >= 0.65:
                rationale = "Strong coverage of expected signals."
                strengths.append(f"{name}: covers {', '.join(matched[:4])}")
            elif raw >= 0.35:
                rationale = "Partial coverage; several important signals are missing."
                gaps.append(f"{name}: partial coverage; add {', '.join(missing[:4])}")
            else:
                rationale = "Weak coverage of this dimension."
                gaps.append(f"{name}: missing {', '.join(missing[:4])}")

            dimension_scores.append(
                DimensionScore(
                    name=name,
                    score=round(score, 3),
                    max_score=max_score,
                    rationale=rationale,
                    matched_signals=matched,
                    missing_signals=missing,
                )
            )

            if raw < 0.65 and dim.get("recommendation"):
                recommendations.append(dim["recommendation"])

        missing_sections = detect_sections(text, self.rubric.get("required_sections", []))
        section_penalty = min(len(missing_sections) * 3, 15)
        base_score = (weighted_points / max(max_points, 1)) * 100
        overall = max(0, round(base_score - section_penalty, 1))

        metadata = {
            "text_length_chars": len(text),
            "required_sections_count": len(self.rubric.get("required_sections", [])),
            "missing_sections_count": len(missing_sections),
            "scoring_mode": "deterministic_rubric_v0"
        }

        return EvalResult(
            metric=self.metric_name,
            overall_score=overall,
            verdict=verdict_for_score(overall),
            dimension_scores=dimension_scores,
            strengths=_dedupe(strengths)[:8],
            gaps=_dedupe(gaps)[:8],
            recommendations=_dedupe(recommendations)[:10],
            missing_sections=missing_sections,
            metadata=metadata,
        )


def _dedupe(items: List[str]) -> List[str]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

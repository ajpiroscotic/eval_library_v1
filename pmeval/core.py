from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import json


@dataclass
class DimensionScore:
    name: str
    score: float
    max_score: float
    rationale: str
    matched_signals: List[str]
    missing_signals: List[str]

    @property
    def percent(self) -> float:
        if self.max_score == 0:
            return 0.0
        return round((self.score / self.max_score) * 100, 2)


@dataclass
class EvalResult:
    metric: str
    overall_score: float
    verdict: str
    dimension_scores: List[DimensionScore]
    strengths: List[str]
    gaps: List[str]
    recommendations: List[str]
    missing_sections: List[str]
    metadata: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def to_markdown(self) -> str:
        lines = []
        lines.append(f"# PM Eval Report: {self.metric}\n")
        lines.append(f"**Overall score:** {self.overall_score}/100")
        lines.append(f"**Verdict:** {self.verdict}\n")

        lines.append("## Dimension scores\n")
        lines.append("| Dimension | Score | Rationale |")
        lines.append("|---|---:|---|")
        for d in self.dimension_scores:
            lines.append(f"| {d.name} | {d.percent}% | {d.rationale} |")

        if self.strengths:
            lines.append("\n## Strong signals\n")
            for item in self.strengths:
                lines.append(f"- {item}")

        if self.gaps:
            lines.append("\n## Gaps\n")
            for item in self.gaps:
                lines.append(f"- {item}")

        if self.missing_sections:
            lines.append("\n## Missing sections\n")
            for item in self.missing_sections:
                lines.append(f"- {item}")

        if self.recommendations:
            lines.append("\n## Recommendations\n")
            for item in self.recommendations:
                lines.append(f"- {item}")

        return "\n".join(lines).strip() + "\n"


def verdict_for_score(score: float) -> str:
    if score >= 85:
        return "Strong — ready for senior review"
    if score >= 70:
        return "Good foundation — improve before launch review"
    if score >= 50:
        return "Needs improvement before stakeholder review"
    return "Weak — missing critical PM/AI launch detail"

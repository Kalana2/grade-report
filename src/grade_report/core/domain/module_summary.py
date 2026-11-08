from dataclasses import dataclass, field


@dataclass
class ModuleSummary:
    "Statistics for one module, produced by the engine"

    module_code: str
    student_count: int
    average: float
    highest: float
    lowest: float
    grade_counts: dict[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.student_count < 1:
            raise ValueError("student_count must be at least 1")
        if not self.lowest <= self.average <= self.highest:
            raise ValueError("expeeted lowest <= average <= highest")

from dataclasses import dataclass


@dataclass(frozen=True)
class StudentMark:
    """One student's mark in one module"""

    index_number: str
    name: str
    module_code: str
    mark: float

    def __post_init__(self) -> None:
        if not self.index_number.strip():
            raise ValueError("index_number must not be empty.")
        if not self.module_code.strip():
            raise ValueError("module_code must not be empty.")
        if not 0 <= self.mark <= 100:
            raise ValueError(f"marks must be between 0 and 100, got {self.mark}")

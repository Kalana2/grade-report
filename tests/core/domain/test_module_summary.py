import pytest

from grade_report.core.domain.module_summary import ModuleSummary


def make_summary(**overrides) -> ModuleSummary:
    values = {
        "module_code": "SCS3311",
        "student_count": 3,
        "average": 60.0,
        "highest": 90.0,
        "lowest": 30.0,
    }
    values.update(overrides)
    return ModuleSummary(**values)


def test_valid_summary_is_created():
    summary = make_summary(grade_counts={"A": 1, "C": 2})
    assert summary.grade_counts == {"A": 1, "C": 2}


def test_grade_counts_are_not_shared_between_instances():
    first = make_summary()
    second = make_summary()
    first.grade_counts["A"] = 1
    assert second.grade_counts == {}


def test_zero_students_is_rejected():
    with pytest.raises(ValueError, match="at least 1"):
        make_summary(student_count=0)


@pytest.mark.parametrize(
    ("average", "highest", "lowest"),
    [
        (95.0, 90.0, 30.0),  # average above highest
        (20.0, 90.0, 30.0),  # average below lowest
        (60.0, 30.0, 90.0),  # highest and lowest swapped
    ],
)
def test_inconsistent_statistics_are_rejected(average, highest, lowest):
    with pytest.raises(ValueError, match="lowest <= average <= highest"):
        make_summary(average=average, highest=highest, lowest=lowest)

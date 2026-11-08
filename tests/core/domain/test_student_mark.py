from dataclasses import FrozenInstanceError

import pytest

from grade_report.core.domain.student_mark import StudentMark


def make_mark(**overrides) -> StudentMark:
    values = {
        "index_number": "2300001",
        "name": "Nimal Perera",
        "module_code": "SCS3311",
        "mark": 75.0,
    }
    values.update(overrides)
    return StudentMark(**values)


def test_valid_mark_is_created():
    mark = make_mark()
    assert mark.module_code == "SCS3311"
    assert mark.mark == 75.0


@pytest.mark.parametrize("value", [0, 50.5, 100])
def test_boundary_marks_are_accepted(value):
    assert make_mark(mark=value).mark == value


@pytest.mark.parametrize("value", [-1, 100.5, 150])
def test_out_of_range_marks_are_rejected(value):
    with pytest.raises(ValueError, match="between 0 and 100"):
        make_mark(mark=value)


@pytest.mark.parametrize("field_name", ["index_number", "module_code"])
@pytest.mark.parametrize("blank", ["", "   "])
def test_blank_identifiers_are_rejected(field_name, blank):
    with pytest.raises(ValueError, match="must not be empty"):
        make_mark(**{field_name: blank})


def test_mark_is_immutable():
    mark = make_mark()
    with pytest.raises(FrozenInstanceError):
        mark.mark = 100

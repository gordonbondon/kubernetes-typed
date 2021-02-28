import os
from typing import List, Tuple, TypedDict

import pytest
from mypy import api


class Expect(TypedDict):
    normal: str
    error: str
    exit_status: int


case_directory = os.path.join(os.path.dirname(__file__), "cases")

cases: List[Tuple[str, Expect]] = [
    (
        "reads_crd.py",
        Expect(
            normal="""
                note: Revealed type is 'TypedDict('Jsonschema', {'spec'?: TypedDict({'cronSpec'?: builtins.str, 'replicas'?: builtins.int})})'
                error: Argument 2 has incompatible type "int"; expected "str"
                error: Argument 2 has incompatible type "str"; expected "int"
            """,
            error="",
            exit_status=1,
        ),
    ),
    (
        "nested_crd.py",
        Expect(
            normal="""
                note: Revealed type is 'TypedDict('Jsonschema', {'stringProperty'?: builtins.str})'
                note: Revealed type is 'builtins.list[TypedDict({'integerProperty'?: builtins.int})]'
                note: Revealed type is 'TypedDict('Jsonschema', {'integerProperty'?: builtins.int})'
                error: Argument 2 has incompatible type "int"; expected "str"
                error: Argument 2 has incompatible type "str"; expected "int"
            """,
            error="",
            exit_status=1,
        ),
    ),
    (
        "wrong_spec.py",
        Expect(
            normal="""
                error: CustomResourceDefinition at tests/crd_typed/cases/wrong_spec.yaml does not have type object subschema defined for ['spec', 'wrongObject']
            """,
            error="",
            exit_status=1,
        ),
    ),
]


@pytest.mark.parametrize("case_file, expected", cases)
def test_cases(case_file: str, expected: Expect):
    normal_report, error_report, exit_status = api.run(
        ["--show-traceback", os.path.join(case_directory, case_file)]
    )

    if expected["error"] == "":
        assert error_report == ""

    for line in expected["normal"].strip().splitlines():
        assert line.strip() in normal_report

    for line in expected["error"].strip().splitlines():
        assert line.strip() in error_report

    assert exit_status == expected["exit_status"]

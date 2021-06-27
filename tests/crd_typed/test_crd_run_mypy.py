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
                8: note: Revealed type is "TypedDict('Jsonschema', {'spec'?: TypedDict({'cronSpec'?: builtins.str, 'replicas'?: builtins.int})})"
                10: error: Value of "cronSpec" has incompatible type "int"; expected "str"
                11: error: Value of "replicas" has incompatible type "str"; expected "int"
            """,
            error="",
            exit_status=1,
        ),
    ),
    (
        "nested_crd.py",
        Expect(
            normal="""
                10: note: Revealed type is "TypedDict('Jsonschema', {'stringProperty'?: builtins.str})"
                11: note: Revealed type is "builtins.list[TypedDict({'integerProperty'?: builtins.int})]"
                12: note: Revealed type is "TypedDict('Jsonschema', {'integerProperty'?: builtins.int})"
                14: error: Value of "stringProperty" has incompatible type "int"; expected "str"
                15: error: Value of "integerProperty" has incompatible type "str"; expected "int"
            """,
            error="",
            exit_status=1,
        ),
    ),
    (
        "wrong_spec.py",
        Expect(
            normal="""
                5: error: CustomResourceDefinition at tests/crd_typed/cases/wrong_spec.yaml does not have type object subschema defined for ['spec', 'wrongObject']
            """,
            error="",
            exit_status=1,
        ),
    ),
]


@pytest.mark.parametrize("case_file, expected", cases)
def test_cases(case_file: str, expected: Expect):
    normal_report, error_report, exit_status = api.run(["--show-traceback", os.path.join(case_directory, case_file)])

    if expected["error"] == "":
        assert error_report == ""

    for line in expected["normal"].strip().splitlines():
        assert line.strip() in normal_report

    for line in expected["error"].strip().splitlines():
        assert line.strip() in error_report

    assert exit_status == expected["exit_status"]

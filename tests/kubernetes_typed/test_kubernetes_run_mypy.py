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
        "read_type.py",
        Expect(
            normal="""
                note: Revealed type is "kubernetes.client.models.v1_container.V1Container"
                note: Revealed type is "kubernetes.client.models.v1_job.V1Job"
                error: "V1Job" has no attribute "status1"; maybe "status"?
            """,
            error="",
            exit_status=1,
        ),
    ),
    (
        "read_builtins.py",
        Expect(
            normal="""
                note: Revealed type is "builtins.str"
                note: Revealed type is "builtins.list[builtins.str]"
                note: Revealed type is "builtins.dict[builtins.str, builtins.list[builtins.str]]"
                note: Revealed type is "datetime.datetime"
                error: Incompatible types in assignment (expression has type "str", variable has type "List[str]")
            """,
            error="",
            exit_status=1,
        ),
    ),
    (
        "read_kubernetes.py",
        Expect(
            normal="""
                error: Argument "name" to "V1Container" has incompatible type "int"; expected "Optional[str]"
                note: Revealed type is "kubernetes.client.models.v1_pod_spec.V1PodSpec"
                note: Revealed type is "builtins.str"
            """,
            error="",
            exit_status=1,
        ),
    ),
    (
        "dict_type.py",
        Expect(
            normal="""
                9: error: Extra key "api_version" for TypedDict "V1PodDict"
                24: note: Revealed type is "builtins.str"
                26: error: Value of "name" has incompatible type "int"; expected "str"
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

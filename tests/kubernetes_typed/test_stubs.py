import subprocess

import pytest

from scripts.generate_utils import PROJECT_DIRECTORY, clone_and_generate
from scripts.stubgen import (
    DEFAULT_BRANCH,
    K8S_CLIENT_MODULE_DIRECTORY,
    K8S_SOURCE_DIRECTORY,
    STUBS_CLIENT_MODULE_DIRECTORY,
    STUBS_TMP_CLIENT_MODULE_DIRECTORY,
    STUBS_TMP_DIRECTORY,
)
from scripts.typeddictgen import DICT_CLIENT_DIRECTORY, generate_dicts

DICT_TMP_CLIENT_DIRECTORY = PROJECT_DIRECTORY / "tmp" / "client"
DICT_TMP_CLIENT_MODELS_DIRECTORY = DICT_TMP_CLIENT_DIRECTORY / "models"


def diff(src: str, dst: str) -> str:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--no-index",
            src,
            dst,
        ],
        stdout=subprocess.PIPE,
    )

    return result.stdout.decode("utf-8")


@pytest.mark.stubtest
def test_generated_stubs():
    clone_and_generate(
        K8S_SOURCE_DIRECTORY,
        K8S_CLIENT_MODULE_DIRECTORY,
        STUBS_TMP_DIRECTORY,
        DEFAULT_BRANCH,
    )

    assert diff(STUBS_TMP_CLIENT_MODULE_DIRECTORY, STUBS_CLIENT_MODULE_DIRECTORY) == ""


@pytest.mark.stubtest
def test_generated_dicts():
    generate_dicts(DICT_TMP_CLIENT_DIRECTORY, DICT_TMP_CLIENT_MODELS_DIRECTORY)

    assert diff(DICT_TMP_CLIENT_DIRECTORY, DICT_CLIENT_DIRECTORY) == ""

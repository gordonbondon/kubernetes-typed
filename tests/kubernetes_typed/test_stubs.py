import subprocess

import pytest

from scripts.generate_utils import clone_and_generate
from scripts.stubgen import (
    DEFAULT_BRANCH,
    K8S_CLIENT_MODULE_DIRECTORY,
    K8S_SOURCE_DIRECTORY,
    STUBS_CLIENT_MODULE_DIRECTORY,
    STUBS_TMP_CLIENT_MODULE_DIRECTORY,
    STUBS_TMP_DIRECTORY,
)


@pytest.mark.stubtest
def test_generated_stubs():
    clone_and_generate(
        K8S_SOURCE_DIRECTORY,
        K8S_CLIENT_MODULE_DIRECTORY,
        STUBS_TMP_DIRECTORY,
        DEFAULT_BRANCH,
    )

    result = subprocess.run(
        [
            "git",
            "diff",
            "--no-index",
            STUBS_TMP_CLIENT_MODULE_DIRECTORY,
            STUBS_CLIENT_MODULE_DIRECTORY,
        ],
        stdout=subprocess.PIPE,
    )

    assert result.stdout.decode("utf-8") == ""

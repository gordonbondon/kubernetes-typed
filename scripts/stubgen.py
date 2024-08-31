#!/usr/bin/env python3
"""Generating mypy stubs."""

import os
import shutil
import sys
from argparse import ArgumentParser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from scripts.generate_utils import PROJECT_DIRECTORY, clone_and_generate

DEFAULT_BRANCH = "release-18.0"

K8S_SOURCE_DIRECTORY = PROJECT_DIRECTORY / "kubernetes-python-source"
K8S_CLIENT_MODULE_DIRECTORY = K8S_SOURCE_DIRECTORY / "kubernetes"
STUBS_TMP_DIRECTORY = PROJECT_DIRECTORY / "stubgen"
STUBS_TMP_CLIENT_MODULE_DIRECTORY = STUBS_TMP_DIRECTORY / "kubernetes"
STUBS_CLIENT_MODULE_DIRECTORY = PROJECT_DIRECTORY / "kubernetes-stubs"

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--kubernetes_python_version", required=False, default=DEFAULT_BRANCH)
    parser.add_argument("--commit_sha", required=False)

    args = parser.parse_args()

    if STUBS_TMP_DIRECTORY.exists():
        shutil.rmtree(STUBS_TMP_DIRECTORY)

    clone_and_generate(
        K8S_SOURCE_DIRECTORY,
        K8S_CLIENT_MODULE_DIRECTORY,
        STUBS_TMP_DIRECTORY,
        args.kubernetes_python_version,
    )

    if STUBS_CLIENT_MODULE_DIRECTORY.exists():
        shutil.rmtree(STUBS_CLIENT_MODULE_DIRECTORY)

    shutil.move(STUBS_TMP_CLIENT_MODULE_DIRECTORY.absolute().as_posix(), STUBS_CLIENT_MODULE_DIRECTORY)

import shutil
import sys
from argparse import ArgumentParser
from pathlib import Path

from git import RemoteProgress, Repo
from mypy.stubgen import generate_stubs, parse_options

PROJECT_DIRECTORY = Path(__file__).parent.parent
K8S_SOURCE_DIRECTORY = PROJECT_DIRECTORY / "kubernetes-python-source"
K8S_CLIENT_MODULE_DIRECTORY = K8S_SOURCE_DIRECTORY / "kubernetes" / "client"
STUBS_TMP_DIRECTORY = PROJECT_DIRECTORY / "stubgen"
STUBS_TMP_CLIENT_MODULE_DIRECTORY = STUBS_TMP_DIRECTORY / "kubernetes" / "client"
STUBS_CLIENT_MODULE_DIRECTORY = PROJECT_DIRECTORY / "kubernetes-stubs" / "client"

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--kubernetes_python_version", required=False, default="12.0")
    parser.add_argument("--commit_sha", required=False)

    args = parser.parse_args()

    branch = f"release-{args.kubernetes_python_version}"
    if K8S_SOURCE_DIRECTORY.exists():
        shutil.rmtree(K8S_SOURCE_DIRECTORY)
    K8S_SOURCE_DIRECTORY.mkdir(exist_ok=True, parents=False)
    repo = Repo.clone_from(
        "https://github.com/kubernetes-client/python.git",
        K8S_SOURCE_DIRECTORY,
        progress=RemoteProgress(),
        branch=branch,
        depth=1,
    )

    stubgen_options = parse_options(
        [
            f"{K8S_CLIENT_MODULE_DIRECTORY}",
            f"-o={STUBS_TMP_DIRECTORY}",
        ]
    )
    generate_stubs(stubgen_options)

    if STUBS_CLIENT_MODULE_DIRECTORY.exists():
        shutil.rmtree(STUBS_CLIENT_MODULE_DIRECTORY)

    shutil.move(STUBS_TMP_CLIENT_MODULE_DIRECTORY, STUBS_CLIENT_MODULE_DIRECTORY)

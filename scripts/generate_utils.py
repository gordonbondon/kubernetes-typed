"""Collection of code generation utils."""

import os
import shutil
from pathlib import Path
from typing import Union

from black import WriteBack, format_file_in_place
from black.mode import Mode
from git import RemoteProgress, Repo
from mypy.stubgen import generate_stubs, parse_options

PROJECT_DIRECTORY = Path(__file__).parent.parent


def format_codegen(dst_dir: Union[str, Path], line_length: int = 180) -> None:
    """Format target files using black."""
    mode = Mode(
        line_length=line_length,
    )

    if isinstance(dst_dir, Path):
        dst_dir = dst_dir.absolute().as_posix()

    for dirpath, _, filenames in os.walk(dst_dir):
        for fn in filenames:
            format_file_in_place(Path(dirpath, fn), True, mode, WriteBack.YES)


def comment_codegen(dst_dir: Union[str, Path], name: str) -> None:
    """Prepend codegen comment to al files in a directory."""
    if isinstance(dst_dir, Path):
        dst_dir = dst_dir.absolute().as_posix()

    for dirpath, _, filenames in os.walk(dst_dir):
        for fn in filenames:
            with open(os.path.join(dirpath, fn), "r") as original:
                file_content = original.read()
            with open(os.path.join(dirpath, fn), "w") as modified:
                modified.write("# Code generated by `{0}`. DO NOT EDIT.\n".format(name) + file_content)


def clone_and_generate(clone_dir: Path, package_dir: Path, dst_dir: Path, branch: str) -> None:
    """Clone source repo and generate stubs for package.

    :param Path clone_dir: Where to clone source repo
    :param Path package_dir: Path to module that needs stubs generated
    :param Path dst_dir: Destination path for stubs
    :param str branch: Which branch to clone
    """
    if clone_dir.exists():
        shutil.rmtree(clone_dir)
    clone_dir.mkdir(exist_ok=True, parents=False)

    repo = Repo.clone_from(
        "https://github.com/kubernetes-client/python.git",
        clone_dir,
        progress=RemoteProgress(),
        branch=branch,
        depth=1,
    )

    for submodule in repo.submodules:
        submodule.update(init=True)

    stubgen_options = parse_options(
        [
            "{0}".format(package_dir),
            "-o={0}".format(dst_dir),
        ],
    )
    generate_stubs(stubgen_options)

    comment_codegen(dst_dir, "stubgen")

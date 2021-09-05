"""kubernetes-typed."""
import os
from typing import List

from setuptools import setup


def find_stub_files(name: str) -> List[str]:
    """Find all files for stubs."""
    stubs = []
    for root, _, files in os.walk(name):
        for stub_file in files:
            if stub_file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    stub_file = os.path.join(sub_root, stub_file)
                stubs.append(stub_file)
    return stubs


tests_require = [
    "black",
    "gitpython==3.1.9",
    "isort",
    "flake8",
    "flake8-black",
    "flake8-isort",
    "jinja2",
    "pytest",
    "tox",
    "tox-gh-actions",
    "wemake-python-styleguide",
]

setup(
    name="kubernetes-typed",
    packages=["crd_typed", "kubernetes_typed", "kubernetes-stubs"],
    package_data={"kubernetes-stubs": find_stub_files("kubernetes-stubs")},
    install_requires=[
        "jsonschema-typed-v2",
        "kubernetes",  # required by PEP 561
        "mypy>=0.800, <=0.910",
        "mypy-extensions",
        "PyYAML",
    ],
    extras_require={"dev": tests_require},
    tests_require=tests_require,
)

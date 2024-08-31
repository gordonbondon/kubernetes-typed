"""kubernetes-typed."""

import os
import pathlib
from typing import List

from setuptools import find_packages, setup

PACKAGE_VERSION = "18.20.1-dev"


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


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

tests_require = [
    "black",
    "gitpython==3.1.43",
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
    version=PACKAGE_VERSION,
    description="Collection of mypy plugins and stubs for kubernetes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Artem Yarmoliuk",
    license="Apache License Version 2.0",
    url="https://github.com/gordonbondon/kubernetes-typed",
    keywords=["Kubernetes", "MyPy", "Stubs", "Typing"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
    packages=[
        "kubernetes-stubs",
        *find_packages(exclude=["kubernetes-python-source", "scripts", "stubgen", "tests", "tmp"]),
    ],
    package_data={
        "crd_typed": ["py.typed"],
        "kubernetes_typed": ["py.typed"],
        "kubernetes-stubs": find_stub_files("kubernetes-stubs"),
    },
    python_requires=">=3.8",
    install_requires=[
        "jsonschema-typed-v2",
        "jsonschema<4.18",
        "mypy>=1.9.0",
        "mypy-extensions>=1.0.0",
        "PyYAML",
    ],
    extras_require={"dev": tests_require, "client": ["kubernetes"]},
    tests_require=tests_require,
    project_urls={  # Optional
        "Bug Reports": "https://github.com/gordonbondon/kubernetes-typed/issues",
        "Source": "https://github.com/gordonbondon/kubernetes-typed",
    },
)

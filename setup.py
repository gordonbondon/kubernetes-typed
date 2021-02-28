import os

from setuptools import setup


def find_stub_files(name):
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


tests_require = [
    "black",
    "gitpython==3.1.9",
    "isort",
    "flake8",
    "flake8-black",
    "flake8-isort",
    "pytest",
    "tox",
    "tox-gh-actions",
]

setup(
    name="kubernetes-typed",
    packages=["crd_typed", "kubernetes_typed", "kubernetes-stubs"],
    package_data={"kubernetes-stubs": find_stub_files("kubernetes-stubs")},
    install_requires=[
        "jsonschema-typed-v2",
        "kubernetes",  # required by PEP 561
        "mypy>=0.750, <=0.812",
        "mypy-extensions",
        "PyYAML",
    ],
    extras_require={"dev": tests_require},
    tests_require=tests_require,
)

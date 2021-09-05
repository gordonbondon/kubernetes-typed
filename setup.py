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

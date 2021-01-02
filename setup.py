from setuptools import setup

tests_require = [
    "black",
    "gitpython==3.1.9",
    "isort",
    "flake8",
    "flake8-black",
    "flake8-isort",
    "kubernetes==12.0.1",
    "pytest",
    "tox",
    "tox-gh-actions",
]

setup(
    name="kubernetes-typed",
    packages=["crd_typed", "kubernetes-stubs"],
    install_requires=[
        "jsonschema-typed-v2",
        "mypy>=0.750, <=0.790",
        "mypy-extensions",
        "PyYAML",
    ],
    extras_require={"dev": tests_require},
    tests_require=tests_require,
)

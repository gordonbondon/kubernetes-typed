# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1LabelSelectorDict

V2beta2MetricIdentifierDict = TypedDict(
    "V2beta2MetricIdentifierDict",
    {
        "name": str,
        "selector": V1LabelSelectorDict,
    },
    total=False,
)
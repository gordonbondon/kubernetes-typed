# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V2beta2MetricIdentifierDict, V2beta2MetricValueStatusDict

V2beta2ExternalMetricStatusDict = TypedDict(
    "V2beta2ExternalMetricStatusDict",
    {
        "current": V2beta2MetricValueStatusDict,
        "metric": V2beta2MetricIdentifierDict,
    },
    total=False,
)

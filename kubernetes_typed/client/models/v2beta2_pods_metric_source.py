# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V2beta2MetricIdentifierDict, V2beta2MetricTargetDict

V2beta2PodsMetricSourceDict = TypedDict(
    "V2beta2PodsMetricSourceDict",
    {
        "metric": V2beta2MetricIdentifierDict,
        "target": V2beta2MetricTargetDict,
    },
    total=False,
)

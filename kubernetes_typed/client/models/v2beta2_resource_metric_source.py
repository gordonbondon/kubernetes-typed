# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V2beta2MetricTargetDict

V2beta2ResourceMetricSourceDict = TypedDict(
    "V2beta2ResourceMetricSourceDict",
    {
        "name": str,
        "target": V2beta2MetricTargetDict,
    },
    total=False,
)

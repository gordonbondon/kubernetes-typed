# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1LabelSelectorDict, V2beta1CrossVersionObjectReferenceDict

V2beta1ObjectMetricStatusDict = TypedDict(
    "V2beta1ObjectMetricStatusDict",
    {
        "averageValue": str,
        "currentValue": str,
        "metricName": str,
        "selector": V1LabelSelectorDict,
        "target": V2beta1CrossVersionObjectReferenceDict,
    },
    total=False,
)

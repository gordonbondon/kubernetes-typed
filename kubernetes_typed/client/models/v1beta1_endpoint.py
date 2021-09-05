# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1EndpointDict generated type."""
from typing import TypedDict, Dict, List

from kubernetes_typed.client import V1ObjectReferenceDict, V1beta1EndpointConditionsDict

V1beta1EndpointDict = TypedDict(
    "V1beta1EndpointDict",
    {
        "addresses": List[str],
        "conditions": V1beta1EndpointConditionsDict,
        "hostname": str,
        "targetRef": V1ObjectReferenceDict,
        "topology": Dict[str, str],
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1EndpointsDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1EndpointSubsetDict, V1ObjectMetaDict

V1EndpointsDict = TypedDict(
    "V1EndpointsDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "subsets": List[V1EndpointSubsetDict],
    },
    total=False,
)

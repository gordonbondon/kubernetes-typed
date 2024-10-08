# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1EndpointsDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1_endpoint_subset import V1EndpointSubsetDict

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

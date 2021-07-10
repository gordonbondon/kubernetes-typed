# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1ObjectMetaDict, V1beta1EndpointDict, V1beta1EndpointPortDict

V1beta1EndpointSliceDict = TypedDict(
    "V1beta1EndpointSliceDict",
    {
        "addressType": str,
        "apiVersion": str,
        "endpoints": List[V1beta1EndpointDict],
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "ports": List[V1beta1EndpointPortDict],
    },
    total=False,
)
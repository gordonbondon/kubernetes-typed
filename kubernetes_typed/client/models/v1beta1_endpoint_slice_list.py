# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1EndpointSliceListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1beta1_endpoint_slice import V1beta1EndpointSliceDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

V1beta1EndpointSliceListDict = TypedDict(
    "V1beta1EndpointSliceListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1EndpointSliceDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

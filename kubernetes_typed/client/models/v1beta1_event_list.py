# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1EventListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1beta1_event import V1beta1EventDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

V1beta1EventListDict = TypedDict(
    "V1beta1EventListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1EventDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

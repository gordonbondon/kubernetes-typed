# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NetworkPolicyListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_network_policy import V1NetworkPolicyDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

V1NetworkPolicyListDict = TypedDict(
    "V1NetworkPolicyListDict",
    {
        "apiVersion": str,
        "items": List[V1NetworkPolicyDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

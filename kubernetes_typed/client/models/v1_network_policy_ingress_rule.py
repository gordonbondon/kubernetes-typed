# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NetworkPolicyIngressRuleDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1NetworkPolicyPeerDict, V1NetworkPolicyPortDict

V1NetworkPolicyIngressRuleDict = TypedDict(
    "V1NetworkPolicyIngressRuleDict",
    {
        "from": List[V1NetworkPolicyPeerDict],
        "ports": List[V1NetworkPolicyPortDict],
    },
    total=False,
)

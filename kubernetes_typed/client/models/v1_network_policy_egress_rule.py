# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NetworkPolicyEgressRuleDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_network_policy_port import V1NetworkPolicyPortDict
from kubernetes_typed.client.models.v1_network_policy_peer import V1NetworkPolicyPeerDict

V1NetworkPolicyEgressRuleDict = TypedDict(
    "V1NetworkPolicyEgressRuleDict",
    {
        "ports": List[V1NetworkPolicyPortDict],
        "to": List[V1NetworkPolicyPeerDict],
    },
    total=False,
)

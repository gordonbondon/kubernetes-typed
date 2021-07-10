# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1LabelSelectorDict, V1beta1NetworkPolicyEgressRuleDict, V1beta1NetworkPolicyIngressRuleDict

V1beta1NetworkPolicySpecDict = TypedDict(
    "V1beta1NetworkPolicySpecDict",
    {
        "egress": List[V1beta1NetworkPolicyEgressRuleDict],
        "ingress": List[V1beta1NetworkPolicyIngressRuleDict],
        "podSelector": V1LabelSelectorDict,
        "policyTypes": List[str],
    },
    total=False,
)
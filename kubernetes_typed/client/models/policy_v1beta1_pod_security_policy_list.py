# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import PolicyV1beta1PodSecurityPolicyDict, V1ListMetaDict

PolicyV1beta1PodSecurityPolicyListDict = TypedDict(
    "PolicyV1beta1PodSecurityPolicyListDict",
    {
        "apiVersion": str,
        "items": List[PolicyV1beta1PodSecurityPolicyDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PodSecurityPolicyListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1beta1_pod_security_policy import V1beta1PodSecurityPolicyDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

V1beta1PodSecurityPolicyListDict = TypedDict(
    "V1beta1PodSecurityPolicyListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1PodSecurityPolicyDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PodSecurityPolicyDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1beta1_pod_security_policy_spec import V1beta1PodSecurityPolicySpecDict

V1beta1PodSecurityPolicyDict = TypedDict(
    "V1beta1PodSecurityPolicyDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1PodSecurityPolicySpecDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NetworkPolicyDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1NetworkPolicySpecDict, V1ObjectMetaDict

V1NetworkPolicyDict = TypedDict(
    "V1NetworkPolicyDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1NetworkPolicySpecDict,
    },
    total=False,
)

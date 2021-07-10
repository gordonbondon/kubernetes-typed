# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1ObjectMetaDict, V1PolicyRuleDict

V1RoleDict = TypedDict(
    "V1RoleDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "rules": List[V1PolicyRuleDict],
    },
    total=False,
)
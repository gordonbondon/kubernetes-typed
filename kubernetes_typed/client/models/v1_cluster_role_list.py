# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ClusterRoleDict, V1ListMetaDict

V1ClusterRoleListDict = TypedDict(
    "V1ClusterRoleListDict",
    {
        "apiVersion": str,
        "items": List[V1ClusterRoleDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

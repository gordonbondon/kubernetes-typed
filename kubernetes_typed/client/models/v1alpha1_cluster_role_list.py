# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1alpha1ClusterRoleDict

V1alpha1ClusterRoleListDict = TypedDict(
    "V1alpha1ClusterRoleListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1ClusterRoleDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

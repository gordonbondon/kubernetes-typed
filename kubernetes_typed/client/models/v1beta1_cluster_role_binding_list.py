# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1ClusterRoleBindingListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1beta1ClusterRoleBindingDict

V1beta1ClusterRoleBindingListDict = TypedDict(
    "V1beta1ClusterRoleBindingListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1ClusterRoleBindingDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

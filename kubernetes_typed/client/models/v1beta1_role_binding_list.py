# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1beta1RoleBindingDict

V1beta1RoleBindingListDict = TypedDict(
    "V1beta1RoleBindingListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1RoleBindingDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

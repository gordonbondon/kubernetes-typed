# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1ListMetaDict, V1alpha1RoleBindingDict

V1alpha1RoleBindingListDict = TypedDict(
    "V1alpha1RoleBindingListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1RoleBindingDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
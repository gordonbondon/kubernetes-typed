# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1alpha1RoleDict

V1alpha1RoleListDict = TypedDict(
    "V1alpha1RoleListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1RoleDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

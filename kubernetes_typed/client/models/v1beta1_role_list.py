# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1beta1RoleDict

V1beta1RoleListDict = TypedDict(
    "V1beta1RoleListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1RoleDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NamespaceListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1NamespaceDict

V1NamespaceListDict = TypedDict(
    "V1NamespaceListDict",
    {
        "apiVersion": str,
        "items": List[V1NamespaceDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

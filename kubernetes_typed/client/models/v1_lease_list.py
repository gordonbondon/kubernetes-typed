# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1LeaseListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1LeaseDict, V1ListMetaDict

V1LeaseListDict = TypedDict(
    "V1LeaseListDict",
    {
        "apiVersion": str,
        "items": List[V1LeaseDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

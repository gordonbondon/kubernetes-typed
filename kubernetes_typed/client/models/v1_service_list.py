# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ServiceListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1ServiceDict

V1ServiceListDict = TypedDict(
    "V1ServiceListDict",
    {
        "apiVersion": str,
        "items": List[V1ServiceDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1ServiceAccountDict

V1ServiceAccountListDict = TypedDict(
    "V1ServiceAccountListDict",
    {
        "apiVersion": str,
        "items": List[V1ServiceAccountDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
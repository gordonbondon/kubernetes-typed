# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1PriorityClassDict

V1PriorityClassListDict = TypedDict(
    "V1PriorityClassListDict",
    {
        "apiVersion": str,
        "items": List[V1PriorityClassDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

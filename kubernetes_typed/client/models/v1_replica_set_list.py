# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1ReplicaSetDict

V1ReplicaSetListDict = TypedDict(
    "V1ReplicaSetListDict",
    {
        "apiVersion": str,
        "items": List[V1ReplicaSetDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

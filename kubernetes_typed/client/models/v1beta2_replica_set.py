# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1ObjectMetaDict, V1beta2ReplicaSetSpecDict, V1beta2ReplicaSetStatusDict

V1beta2ReplicaSetDict = TypedDict(
    "V1beta2ReplicaSetDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta2ReplicaSetSpecDict,
        "status": V1beta2ReplicaSetStatusDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1ObjectMetaDict, V1PersistentVolumeClaimSpecDict, V1PersistentVolumeClaimStatusDict

V1PersistentVolumeClaimDict = TypedDict(
    "V1PersistentVolumeClaimDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1PersistentVolumeClaimSpecDict,
        "status": V1PersistentVolumeClaimStatusDict,
    },
    total=False,
)
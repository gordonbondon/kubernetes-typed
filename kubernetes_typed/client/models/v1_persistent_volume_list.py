# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1ListMetaDict, V1PersistentVolumeDict

V1PersistentVolumeListDict = TypedDict(
    "V1PersistentVolumeListDict",
    {
        "apiVersion": str,
        "items": List[V1PersistentVolumeDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1ObjectMetaDict, V1beta2ScaleSpecDict, V1beta2ScaleStatusDict

V1beta2ScaleDict = TypedDict(
    "V1beta2ScaleDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta2ScaleSpecDict,
        "status": V1beta2ScaleStatusDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1ObjectMetaDict, V1TokenRequestSpecDict, V1TokenRequestStatusDict

V1TokenRequestDict = TypedDict(
    "V1TokenRequestDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1TokenRequestSpecDict,
        "status": V1TokenRequestStatusDict,
    },
    total=False,
)
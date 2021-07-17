# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ListMetaDict, V1StatusDetailsDict

V1StatusDict = TypedDict(
    "V1StatusDict",
    {
        "apiVersion": str,
        "code": int,
        "details": V1StatusDetailsDict,
        "kind": str,
        "message": str,
        "metadata": V1ListMetaDict,
        "reason": str,
        "status": str,
    },
    total=False,
)

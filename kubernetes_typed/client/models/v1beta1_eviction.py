# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1DeleteOptionsDict, V1ObjectMetaDict

V1beta1EvictionDict = TypedDict(
    "V1beta1EvictionDict",
    {
        "apiVersion": str,
        "deleteOptions": V1DeleteOptionsDict,
        "kind": str,
        "metadata": V1ObjectMetaDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict

V1beta1ControllerRevisionDict = TypedDict(
    "V1beta1ControllerRevisionDict",
    {
        "apiVersion": str,
        "data": object,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "revision": int,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1beta2ControllerRevisionDict

V1beta2ControllerRevisionListDict = TypedDict(
    "V1beta2ControllerRevisionListDict",
    {
        "apiVersion": str,
        "items": List[V1beta2ControllerRevisionDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1NodeSelectorTermDict

V1NodeSelectorDict = TypedDict(
    "V1NodeSelectorDict",
    {
        "nodeSelectorTerms": List[V1NodeSelectorTermDict],
    },
    total=False,
)
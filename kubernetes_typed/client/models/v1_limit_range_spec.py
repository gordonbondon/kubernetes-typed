# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1LimitRangeItemDict

V1LimitRangeSpecDict = TypedDict(
    "V1LimitRangeSpecDict",
    {
        "limits": List[V1LimitRangeItemDict],
    },
    total=False,
)
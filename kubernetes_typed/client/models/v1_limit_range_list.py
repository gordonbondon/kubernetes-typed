# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1LimitRangeListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1LimitRangeDict, V1ListMetaDict

V1LimitRangeListDict = TypedDict(
    "V1LimitRangeListDict",
    {
        "apiVersion": str,
        "items": List[V1LimitRangeDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

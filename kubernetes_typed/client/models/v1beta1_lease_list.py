# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1ListMetaDict, V1beta1LeaseDict

V1beta1LeaseListDict = TypedDict(
    "V1beta1LeaseListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1LeaseDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
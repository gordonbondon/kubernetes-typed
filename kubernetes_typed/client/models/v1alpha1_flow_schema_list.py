# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1alpha1FlowSchemaDict

V1alpha1FlowSchemaListDict = TypedDict(
    "V1alpha1FlowSchemaListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1FlowSchemaDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

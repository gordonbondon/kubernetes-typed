# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1CustomResourceDefinitionDict, V1ListMetaDict

V1CustomResourceDefinitionListDict = TypedDict(
    "V1CustomResourceDefinitionListDict",
    {
        "apiVersion": str,
        "items": List[V1CustomResourceDefinitionDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
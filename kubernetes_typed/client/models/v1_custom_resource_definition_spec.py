# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1CustomResourceConversionDict, V1CustomResourceDefinitionNamesDict, V1CustomResourceDefinitionVersionDict

V1CustomResourceDefinitionSpecDict = TypedDict(
    "V1CustomResourceDefinitionSpecDict",
    {
        "conversion": V1CustomResourceConversionDict,
        "group": str,
        "names": V1CustomResourceDefinitionNamesDict,
        "preserveUnknownFields": bool,
        "scope": str,
        "versions": List[V1CustomResourceDefinitionVersionDict],
    },
    total=False,
)
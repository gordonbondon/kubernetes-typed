# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CustomResourceDefinitionDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1CustomResourceDefinitionSpecDict, V1CustomResourceDefinitionStatusDict, V1ObjectMetaDict

V1CustomResourceDefinitionDict = TypedDict(
    "V1CustomResourceDefinitionDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1CustomResourceDefinitionSpecDict,
        "status": V1CustomResourceDefinitionStatusDict,
    },
    total=False,
)

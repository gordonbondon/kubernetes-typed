# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CustomResourceDefinitionDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1beta1CustomResourceDefinitionSpecDict, V1beta1CustomResourceDefinitionStatusDict

V1beta1CustomResourceDefinitionDict = TypedDict(
    "V1beta1CustomResourceDefinitionDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1CustomResourceDefinitionSpecDict,
        "status": V1beta1CustomResourceDefinitionStatusDict,
    },
    total=False,
)

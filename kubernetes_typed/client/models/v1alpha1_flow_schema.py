# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1FlowSchemaDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1alpha1FlowSchemaSpecDict, V1alpha1FlowSchemaStatusDict

V1alpha1FlowSchemaDict = TypedDict(
    "V1alpha1FlowSchemaDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1alpha1FlowSchemaSpecDict,
        "status": V1alpha1FlowSchemaStatusDict,
    },
    total=False,
)

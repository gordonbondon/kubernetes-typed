# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1EvictionDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_delete_options import V1DeleteOptionsDict
from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict

V1beta1EvictionDict = TypedDict(
    "V1beta1EvictionDict",
    {
        "apiVersion": str,
        "deleteOptions": V1DeleteOptionsDict,
        "kind": str,
        "metadata": V1ObjectMetaDict,
    },
    total=False,
)

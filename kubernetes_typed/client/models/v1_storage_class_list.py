# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1StorageClassListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_storage_class import V1StorageClassDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

V1StorageClassListDict = TypedDict(
    "V1StorageClassListDict",
    {
        "apiVersion": str,
        "items": List[V1StorageClassDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

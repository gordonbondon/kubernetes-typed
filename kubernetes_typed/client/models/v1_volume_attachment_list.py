# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1VolumeAttachmentDict

V1VolumeAttachmentListDict = TypedDict(
    "V1VolumeAttachmentListDict",
    {
        "apiVersion": str,
        "items": List[V1VolumeAttachmentDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
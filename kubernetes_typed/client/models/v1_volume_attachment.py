# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1VolumeAttachmentSpecDict, V1VolumeAttachmentStatusDict

V1VolumeAttachmentDict = TypedDict(
    "V1VolumeAttachmentDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1VolumeAttachmentSpecDict,
        "status": V1VolumeAttachmentStatusDict,
    },
    total=False,
)

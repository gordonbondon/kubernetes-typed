# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1alpha1VolumeAttachmentSpecDict, V1alpha1VolumeAttachmentStatusDict

V1alpha1VolumeAttachmentDict = TypedDict(
    "V1alpha1VolumeAttachmentDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1alpha1VolumeAttachmentSpecDict,
        "status": V1alpha1VolumeAttachmentStatusDict,
    },
    total=False,
)

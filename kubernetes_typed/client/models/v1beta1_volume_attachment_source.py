# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1PersistentVolumeSpecDict

V1beta1VolumeAttachmentSourceDict = TypedDict(
    "V1beta1VolumeAttachmentSourceDict",
    {
        "inlineVolumeSpec": V1PersistentVolumeSpecDict,
        "persistentVolumeName": str,
    },
    total=False,
)

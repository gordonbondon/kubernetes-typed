# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1LocalObjectReferenceDict

V1CinderVolumeSourceDict = TypedDict(
    "V1CinderVolumeSourceDict",
    {
        "fsType": str,
        "readOnly": bool,
        "secretRef": V1LocalObjectReferenceDict,
        "volumeID": str,
    },
    total=False,
)

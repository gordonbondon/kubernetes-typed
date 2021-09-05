# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CSIVolumeSourceDict generated type."""
from typing import TypedDict, Dict

from kubernetes_typed.client import V1LocalObjectReferenceDict

V1CSIVolumeSourceDict = TypedDict(
    "V1CSIVolumeSourceDict",
    {
        "driver": str,
        "fsType": str,
        "nodePublishSecretRef": V1LocalObjectReferenceDict,
        "readOnly": bool,
        "volumeAttributes": Dict[str, str],
    },
    total=False,
)

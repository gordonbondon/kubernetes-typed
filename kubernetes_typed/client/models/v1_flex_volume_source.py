# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, Dict

from kubernetes_typed.client import V1LocalObjectReferenceDict

V1FlexVolumeSourceDict = TypedDict(
    "V1FlexVolumeSourceDict",
    {
        "driver": str,
        "fsType": str,
        "options": Dict[str, str],
        "readOnly": bool,
        "secretRef": V1LocalObjectReferenceDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ConfigMapVolumeSourceDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_key_to_path import V1KeyToPathDict

V1ConfigMapVolumeSourceDict = TypedDict(
    "V1ConfigMapVolumeSourceDict",
    {
        "defaultMode": int,
        "items": List[V1KeyToPathDict],
        "name": str,
        "optional": bool,
    },
    total=False,
)

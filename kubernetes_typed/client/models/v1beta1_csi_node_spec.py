# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CSINodeSpecDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1beta1CSINodeDriverDict

V1beta1CSINodeSpecDict = TypedDict(
    "V1beta1CSINodeSpecDict",
    {
        "drivers": List[V1beta1CSINodeDriverDict],
    },
    total=False,
)

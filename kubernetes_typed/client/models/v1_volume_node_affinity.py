# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1VolumeNodeAffinityDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1NodeSelectorDict

V1VolumeNodeAffinityDict = TypedDict(
    "V1VolumeNodeAffinityDict",
    {
        "required": V1NodeSelectorDict,
    },
    total=False,
)

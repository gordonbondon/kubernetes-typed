# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TopologySelectorTermDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1TopologySelectorLabelRequirementDict

V1TopologySelectorTermDict = TypedDict(
    "V1TopologySelectorTermDict",
    {
        "matchLabelExpressions": List[V1TopologySelectorLabelRequirementDict],
    },
    total=False,
)

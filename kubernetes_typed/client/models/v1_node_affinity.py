# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NodeAffinityDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_preferred_scheduling_term import V1PreferredSchedulingTermDict
from kubernetes_typed.client.models.v1_node_selector import V1NodeSelectorDict

V1NodeAffinityDict = TypedDict(
    "V1NodeAffinityDict",
    {
        "preferredDuringSchedulingIgnoredDuringExecution": List[V1PreferredSchedulingTermDict],
        "requiredDuringSchedulingIgnoredDuringExecution": V1NodeSelectorDict,
    },
    total=False,
)

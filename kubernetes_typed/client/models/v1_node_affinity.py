# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1NodeSelectorDict, V1PreferredSchedulingTermDict

V1NodeAffinityDict = TypedDict(
    "V1NodeAffinityDict",
    {
        "preferredDuringSchedulingIgnoredDuringExecution": List[V1PreferredSchedulingTermDict],
        "requiredDuringSchedulingIgnoredDuringExecution": V1NodeSelectorDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1PodAffinityTermDict, V1WeightedPodAffinityTermDict

V1PodAffinityDict = TypedDict(
    "V1PodAffinityDict",
    {
        "preferredDuringSchedulingIgnoredDuringExecution": List[V1WeightedPodAffinityTermDict],
        "requiredDuringSchedulingIgnoredDuringExecution": List[V1PodAffinityTermDict],
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1RuntimeClassSpecDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1alpha1_overhead import V1alpha1OverheadDict
from kubernetes_typed.client.models.v1alpha1_scheduling import V1alpha1SchedulingDict

V1alpha1RuntimeClassSpecDict = TypedDict(
    "V1alpha1RuntimeClassSpecDict",
    {
        "overhead": V1alpha1OverheadDict,
        "runtimeHandler": str,
        "scheduling": V1alpha1SchedulingDict,
    },
    total=False,
)

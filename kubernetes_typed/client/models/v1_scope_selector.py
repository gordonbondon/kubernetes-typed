# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ScopedResourceSelectorRequirementDict

V1ScopeSelectorDict = TypedDict(
    "V1ScopeSelectorDict",
    {
        "matchExpressions": List[V1ScopedResourceSelectorRequirementDict],
    },
    total=False,
)
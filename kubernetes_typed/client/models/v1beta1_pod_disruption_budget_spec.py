# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1LabelSelectorDict

V1beta1PodDisruptionBudgetSpecDict = TypedDict(
    "V1beta1PodDisruptionBudgetSpecDict",
    {
        "maxUnavailable": object,
        "minAvailable": object,
        "selector": V1LabelSelectorDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1LabelSelectorDict

V1alpha1AggregationRuleDict = TypedDict(
    "V1alpha1AggregationRuleDict",
    {
        "clusterRoleSelectors": List[V1LabelSelectorDict],
    },
    total=False,
)

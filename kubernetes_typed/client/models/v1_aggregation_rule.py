# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1LabelSelectorDict

V1AggregationRuleDict = TypedDict(
    "V1AggregationRuleDict",
    {
        "clusterRoleSelectors": List[V1LabelSelectorDict],
    },
    total=False,
)
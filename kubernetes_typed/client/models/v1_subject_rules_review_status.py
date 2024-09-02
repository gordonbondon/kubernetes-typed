# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1SubjectRulesReviewStatusDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_non_resource_rule import V1NonResourceRuleDict
from kubernetes_typed.client.models.v1_resource_rule import V1ResourceRuleDict

V1SubjectRulesReviewStatusDict = TypedDict(
    "V1SubjectRulesReviewStatusDict",
    {
        "evaluationError": str,
        "incomplete": bool,
        "nonResourceRules": List[V1NonResourceRuleDict],
        "resourceRules": List[V1ResourceRuleDict],
    },
    total=False,
)

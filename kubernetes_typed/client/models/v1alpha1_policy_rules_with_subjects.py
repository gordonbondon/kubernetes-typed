# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1PolicyRulesWithSubjectsDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import FlowcontrolV1alpha1SubjectDict, V1alpha1NonResourcePolicyRuleDict, V1alpha1ResourcePolicyRuleDict

V1alpha1PolicyRulesWithSubjectsDict = TypedDict(
    "V1alpha1PolicyRulesWithSubjectsDict",
    {
        "nonResourceRules": List[V1alpha1NonResourcePolicyRuleDict],
        "resourceRules": List[V1alpha1ResourcePolicyRuleDict],
        "subjects": List[FlowcontrolV1alpha1SubjectDict],
    },
    total=False,
)

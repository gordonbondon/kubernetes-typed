# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1FlowSchemaSpecDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1alpha1_flow_distinguisher_method import V1alpha1FlowDistinguisherMethodDict
from kubernetes_typed.client.models.v1alpha1_priority_level_configuration_reference import V1alpha1PriorityLevelConfigurationReferenceDict
from kubernetes_typed.client.models.v1alpha1_policy_rules_with_subjects import V1alpha1PolicyRulesWithSubjectsDict

V1alpha1FlowSchemaSpecDict = TypedDict(
    "V1alpha1FlowSchemaSpecDict",
    {
        "distinguisherMethod": V1alpha1FlowDistinguisherMethodDict,
        "matchingPrecedence": int,
        "priorityLevelConfiguration": V1alpha1PriorityLevelConfigurationReferenceDict,
        "rules": List[V1alpha1PolicyRulesWithSubjectsDict],
    },
    total=False,
)

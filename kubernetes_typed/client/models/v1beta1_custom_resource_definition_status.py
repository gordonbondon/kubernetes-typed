# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CustomResourceDefinitionStatusDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1beta1_custom_resource_definition_names import V1beta1CustomResourceDefinitionNamesDict
from kubernetes_typed.client.models.v1beta1_custom_resource_definition_condition import V1beta1CustomResourceDefinitionConditionDict

V1beta1CustomResourceDefinitionStatusDict = TypedDict(
    "V1beta1CustomResourceDefinitionStatusDict",
    {
        "acceptedNames": V1beta1CustomResourceDefinitionNamesDict,
        "conditions": List[V1beta1CustomResourceDefinitionConditionDict],
        "storedVersions": List[str],
    },
    total=False,
)

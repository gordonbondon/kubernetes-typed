# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1PriorityLevelConfigurationDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1alpha1_priority_level_configuration_spec import V1alpha1PriorityLevelConfigurationSpecDict
from kubernetes_typed.client.models.v1alpha1_priority_level_configuration_status import V1alpha1PriorityLevelConfigurationStatusDict

V1alpha1PriorityLevelConfigurationDict = TypedDict(
    "V1alpha1PriorityLevelConfigurationDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1alpha1PriorityLevelConfigurationSpecDict,
        "status": V1alpha1PriorityLevelConfigurationStatusDict,
    },
    total=False,
)

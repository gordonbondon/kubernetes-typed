# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1PriorityLevelConfigurationDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1alpha1PriorityLevelConfigurationSpecDict, V1alpha1PriorityLevelConfigurationStatusDict

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

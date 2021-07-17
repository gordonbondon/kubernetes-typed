# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1LabelSelectorDict, V1PersistentVolumeClaimDict, V1PodTemplateSpecDict, V1beta2StatefulSetUpdateStrategyDict

V1beta2StatefulSetSpecDict = TypedDict(
    "V1beta2StatefulSetSpecDict",
    {
        "podManagementPolicy": str,
        "replicas": int,
        "revisionHistoryLimit": int,
        "selector": V1LabelSelectorDict,
        "serviceName": str,
        "template": V1PodTemplateSpecDict,
        "updateStrategy": V1beta2StatefulSetUpdateStrategyDict,
        "volumeClaimTemplates": List[V1PersistentVolumeClaimDict],
    },
    total=False,
)

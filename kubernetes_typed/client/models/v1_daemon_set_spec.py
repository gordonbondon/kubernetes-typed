# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1DaemonSetSpecDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1DaemonSetUpdateStrategyDict, V1LabelSelectorDict, V1PodTemplateSpecDict

V1DaemonSetSpecDict = TypedDict(
    "V1DaemonSetSpecDict",
    {
        "minReadySeconds": int,
        "revisionHistoryLimit": int,
        "selector": V1LabelSelectorDict,
        "template": V1PodTemplateSpecDict,
        "updateStrategy": V1DaemonSetUpdateStrategyDict,
    },
    total=False,
)

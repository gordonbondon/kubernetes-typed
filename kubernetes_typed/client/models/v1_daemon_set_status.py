# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1DaemonSetConditionDict

V1DaemonSetStatusDict = TypedDict(
    "V1DaemonSetStatusDict",
    {
        "collisionCount": int,
        "conditions": List[V1DaemonSetConditionDict],
        "currentNumberScheduled": int,
        "desiredNumberScheduled": int,
        "numberAvailable": int,
        "numberMisscheduled": int,
        "numberReady": int,
        "numberUnavailable": int,
        "observedGeneration": int,
        "updatedNumberScheduled": int,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1RollingUpdateDaemonSetDict

V1DaemonSetUpdateStrategyDict = TypedDict(
    "V1DaemonSetUpdateStrategyDict",
    {
        "rollingUpdate": V1RollingUpdateDaemonSetDict,
        "type": str,
    },
    total=False,
)
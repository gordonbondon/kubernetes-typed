# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1beta1RollingUpdateDaemonSetDict

V1beta1DaemonSetUpdateStrategyDict = TypedDict(
    "V1beta1DaemonSetUpdateStrategyDict",
    {
        "rollingUpdate": V1beta1RollingUpdateDaemonSetDict,
        "type": str,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1DeploymentStrategyDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_rolling_update_deployment import V1RollingUpdateDeploymentDict

V1DeploymentStrategyDict = TypedDict(
    "V1DeploymentStrategyDict",
    {
        "rollingUpdate": V1RollingUpdateDeploymentDict,
        "type": str,
    },
    total=False,
)

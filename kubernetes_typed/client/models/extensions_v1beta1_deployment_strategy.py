# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import ExtensionsV1beta1RollingUpdateDeploymentDict

ExtensionsV1beta1DeploymentStrategyDict = TypedDict(
    "ExtensionsV1beta1DeploymentStrategyDict",
    {
        "rollingUpdate": ExtensionsV1beta1RollingUpdateDeploymentDict,
        "type": str,
    },
    total=False,
)
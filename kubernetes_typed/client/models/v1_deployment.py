# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1DeploymentSpecDict, V1DeploymentStatusDict, V1ObjectMetaDict

V1DeploymentDict = TypedDict(
    "V1DeploymentDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1DeploymentSpecDict,
        "status": V1DeploymentStatusDict,
    },
    total=False,
)
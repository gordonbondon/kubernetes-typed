# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, Dict

from kubernetes_typed.client import ExtensionsV1beta1RollbackConfigDict

ExtensionsV1beta1DeploymentRollbackDict = TypedDict(
    "ExtensionsV1beta1DeploymentRollbackDict",
    {
        "apiVersion": str,
        "kind": str,
        "name": str,
        "rollbackTo": ExtensionsV1beta1RollbackConfigDict,
        "updatedAnnotations": Dict[str, str],
    },
    total=False,
)

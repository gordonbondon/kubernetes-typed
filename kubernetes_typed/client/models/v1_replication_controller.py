# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ReplicationControllerDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1ReplicationControllerSpecDict, V1ReplicationControllerStatusDict

V1ReplicationControllerDict = TypedDict(
    "V1ReplicationControllerDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1ReplicationControllerSpecDict,
        "status": V1ReplicationControllerStatusDict,
    },
    total=False,
)

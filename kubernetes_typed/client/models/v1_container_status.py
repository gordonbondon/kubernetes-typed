# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1ContainerStateDict

V1ContainerStatusDict = TypedDict(
    "V1ContainerStatusDict",
    {
        "containerID": str,
        "image": str,
        "imageID": str,
        "lastState": V1ContainerStateDict,
        "name": str,
        "ready": bool,
        "restartCount": int,
        "started": bool,
        "state": V1ContainerStateDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ContainerStateTerminatedDict generated type."""
import datetime
from typing import TypedDict

V1ContainerStateTerminatedDict = TypedDict(
    "V1ContainerStateTerminatedDict",
    {
        "containerID": str,
        "exitCode": int,
        "finishedAt": datetime.datetime,
        "message": str,
        "reason": str,
        "signal": int,
        "startedAt": datetime.datetime,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodConditionDict generated type."""
import datetime
from typing import TypedDict

V1PodConditionDict = TypedDict(
    "V1PodConditionDict",
    {
        "lastProbeTime": datetime.datetime,
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)

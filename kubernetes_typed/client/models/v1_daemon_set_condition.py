# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1DaemonSetConditionDict generated type."""
import datetime
from typing import TypedDict

V1DaemonSetConditionDict = TypedDict(
    "V1DaemonSetConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)

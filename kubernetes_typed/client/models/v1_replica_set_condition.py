# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ReplicaSetConditionDict generated type."""
import datetime
from typing import TypedDict

V1ReplicaSetConditionDict = TypedDict(
    "V1ReplicaSetConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
import datetime
from typing import TypedDict


V1JobConditionDict = TypedDict(
    "V1JobConditionDict",
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
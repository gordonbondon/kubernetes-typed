# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1APIServiceConditionDict generated type."""
import datetime
from typing import TypedDict

V1APIServiceConditionDict = TypedDict(
    "V1APIServiceConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)

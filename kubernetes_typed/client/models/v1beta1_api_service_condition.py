# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1APIServiceConditionDict generated type."""
import datetime
from typing import TypedDict

V1beta1APIServiceConditionDict = TypedDict(
    "V1beta1APIServiceConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)

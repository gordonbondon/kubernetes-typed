# Code generated by `typeddictgen`. DO NOT EDIT.
import datetime
from typing import TypedDict

V2beta2HorizontalPodAutoscalerConditionDict = TypedDict(
    "V2beta2HorizontalPodAutoscalerConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)
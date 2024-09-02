# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1JobStatusDict generated type."""
import datetime
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_job_condition import V1JobConditionDict

V1JobStatusDict = TypedDict(
    "V1JobStatusDict",
    {
        "active": int,
        "completionTime": datetime.datetime,
        "conditions": List[V1JobConditionDict],
        "failed": int,
        "startTime": datetime.datetime,
        "succeeded": int,
    },
    total=False,
)

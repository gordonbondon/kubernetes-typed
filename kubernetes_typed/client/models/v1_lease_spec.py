# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1LeaseSpecDict generated type."""
import datetime
from typing import TypedDict

V1LeaseSpecDict = TypedDict(
    "V1LeaseSpecDict",
    {
        "acquireTime": datetime.datetime,
        "holderIdentity": str,
        "leaseDurationSeconds": int,
        "leaseTransitions": int,
        "renewTime": datetime.datetime,
    },
    total=False,
)

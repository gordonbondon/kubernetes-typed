# Code generated by `typeddictgen`. DO NOT EDIT.
import datetime
from typing import TypedDict

V1beta1LeaseSpecDict = TypedDict(
    "V1beta1LeaseSpecDict",
    {
        "acquireTime": datetime.datetime,
        "holderIdentity": str,
        "leaseDurationSeconds": int,
        "leaseTransitions": int,
        "renewTime": datetime.datetime,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TokenRequestStatusDict generated type."""
import datetime
from typing import TypedDict

V1TokenRequestStatusDict = TypedDict(
    "V1TokenRequestStatusDict",
    {
        "expirationTimestamp": datetime.datetime,
        "token": str,
    },
    total=False,
)

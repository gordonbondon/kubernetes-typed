# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TaintDict generated type."""
import datetime
from typing import TypedDict

V1TaintDict = TypedDict(
    "V1TaintDict",
    {
        "effect": str,
        "key": str,
        "timeAdded": datetime.datetime,
        "value": str,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TolerationDict generated type."""
from typing import TypedDict

V1TolerationDict = TypedDict(
    "V1TolerationDict",
    {
        "effect": str,
        "key": str,
        "operator": str,
        "tolerationSeconds": int,
        "value": str,
    },
    total=False,
)

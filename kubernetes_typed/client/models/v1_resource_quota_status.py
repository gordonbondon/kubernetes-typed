# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ResourceQuotaStatusDict generated type."""
from typing import TypedDict, Dict

V1ResourceQuotaStatusDict = TypedDict(
    "V1ResourceQuotaStatusDict",
    {
        "hard": Dict[str, str],
        "used": Dict[str, str],
    },
    total=False,
)

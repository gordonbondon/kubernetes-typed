# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ResourceRequirementsDict generated type."""
from typing import TypedDict, Dict

V1ResourceRequirementsDict = TypedDict(
    "V1ResourceRequirementsDict",
    {
        "limits": Dict[str, str],
        "requests": Dict[str, str],
    },
    total=False,
)

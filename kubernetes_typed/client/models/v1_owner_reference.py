# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1OwnerReferenceDict generated type."""
from typing import TypedDict

V1OwnerReferenceDict = TypedDict(
    "V1OwnerReferenceDict",
    {
        "apiVersion": str,
        "blockOwnerDeletion": bool,
        "controller": bool,
        "kind": str,
        "name": str,
        "uid": str,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

V1SubjectAccessReviewStatusDict = TypedDict(
    "V1SubjectAccessReviewStatusDict",
    {
        "allowed": bool,
        "denied": bool,
        "evaluationError": str,
        "reason": str,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1SubjectAccessReviewStatusDict generated type."""
from typing import TypedDict

V1beta1SubjectAccessReviewStatusDict = TypedDict(
    "V1beta1SubjectAccessReviewStatusDict",
    {
        "allowed": bool,
        "denied": bool,
        "evaluationError": str,
        "reason": str,
    },
    total=False,
)

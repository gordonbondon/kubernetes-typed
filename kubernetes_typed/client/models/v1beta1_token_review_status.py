# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1beta1UserInfoDict

V1beta1TokenReviewStatusDict = TypedDict(
    "V1beta1TokenReviewStatusDict",
    {
        "audiences": List[str],
        "authenticated": bool,
        "error": str,
        "user": V1beta1UserInfoDict,
    },
    total=False,
)

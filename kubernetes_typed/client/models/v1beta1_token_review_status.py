# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1TokenReviewStatusDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1beta1_user_info import V1beta1UserInfoDict

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

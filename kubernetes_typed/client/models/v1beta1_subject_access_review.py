# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1SubjectAccessReviewDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1beta1SubjectAccessReviewSpecDict, V1beta1SubjectAccessReviewStatusDict

V1beta1SubjectAccessReviewDict = TypedDict(
    "V1beta1SubjectAccessReviewDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1SubjectAccessReviewSpecDict,
        "status": V1beta1SubjectAccessReviewStatusDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1beta1SelfSubjectAccessReviewSpecDict, V1beta1SubjectAccessReviewStatusDict

V1beta1SelfSubjectAccessReviewDict = TypedDict(
    "V1beta1SelfSubjectAccessReviewDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1SelfSubjectAccessReviewSpecDict,
        "status": V1beta1SubjectAccessReviewStatusDict,
    },
    total=False,
)

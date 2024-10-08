# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1SelfSubjectAccessReviewDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1_self_subject_access_review_spec import V1SelfSubjectAccessReviewSpecDict
from kubernetes_typed.client.models.v1_subject_access_review_status import V1SubjectAccessReviewStatusDict

V1SelfSubjectAccessReviewDict = TypedDict(
    "V1SelfSubjectAccessReviewDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1SelfSubjectAccessReviewSpecDict,
        "status": V1SubjectAccessReviewStatusDict,
    },
    total=False,
)

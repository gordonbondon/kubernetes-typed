# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1SubjectAccessReviewDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1_subject_access_review_spec import V1SubjectAccessReviewSpecDict
from kubernetes_typed.client.models.v1_subject_access_review_status import V1SubjectAccessReviewStatusDict

V1SubjectAccessReviewDict = TypedDict(
    "V1SubjectAccessReviewDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1SubjectAccessReviewSpecDict,
        "status": V1SubjectAccessReviewStatusDict,
    },
    total=False,
)

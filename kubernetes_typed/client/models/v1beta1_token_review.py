# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1ObjectMetaDict, V1beta1TokenReviewSpecDict, V1beta1TokenReviewStatusDict

V1beta1TokenReviewDict = TypedDict(
    "V1beta1TokenReviewDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1TokenReviewSpecDict,
        "status": V1beta1TokenReviewStatusDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import ApiregistrationV1beta1ServiceReferenceDict

V1beta1APIServiceSpecDict = TypedDict(
    "V1beta1APIServiceSpecDict",
    {
        "caBundle": str,
        "group": str,
        "groupPriorityMinimum": int,
        "insecureSkipTLSVerify": bool,
        "service": ApiregistrationV1beta1ServiceReferenceDict,
        "version": str,
        "versionPriority": int,
    },
    total=False,
)
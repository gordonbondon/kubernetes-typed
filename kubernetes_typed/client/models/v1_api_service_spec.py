# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import ApiregistrationV1ServiceReferenceDict

V1APIServiceSpecDict = TypedDict(
    "V1APIServiceSpecDict",
    {
        "caBundle": str,
        "group": str,
        "groupPriorityMinimum": int,
        "insecureSkipTLSVerify": bool,
        "service": ApiregistrationV1ServiceReferenceDict,
        "version": str,
        "versionPriority": int,
    },
    total=False,
)
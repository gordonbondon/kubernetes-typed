# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1AuditSinkSpecDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1alpha1PolicyDict, V1alpha1WebhookDict

V1alpha1AuditSinkSpecDict = TypedDict(
    "V1alpha1AuditSinkSpecDict",
    {
        "policy": V1alpha1PolicyDict,
        "webhook": V1alpha1WebhookDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1WebhookClientConfigDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1alpha1ServiceReferenceDict

V1alpha1WebhookClientConfigDict = TypedDict(
    "V1alpha1WebhookClientConfigDict",
    {
        "caBundle": str,
        "service": V1alpha1ServiceReferenceDict,
        "url": str,
    },
    total=False,
)

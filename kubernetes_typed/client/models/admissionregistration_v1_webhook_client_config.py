# Code generated by `typeddictgen`. DO NOT EDIT.
"""AdmissionregistrationV1WebhookClientConfigDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import AdmissionregistrationV1ServiceReferenceDict

AdmissionregistrationV1WebhookClientConfigDict = TypedDict(
    "AdmissionregistrationV1WebhookClientConfigDict",
    {
        "caBundle": str,
        "service": AdmissionregistrationV1ServiceReferenceDict,
        "url": str,
    },
    total=False,
)

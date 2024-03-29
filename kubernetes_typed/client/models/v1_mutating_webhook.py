# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1MutatingWebhookDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import AdmissionregistrationV1WebhookClientConfigDict, V1LabelSelectorDict, V1RuleWithOperationsDict

V1MutatingWebhookDict = TypedDict(
    "V1MutatingWebhookDict",
    {
        "admissionReviewVersions": List[str],
        "clientConfig": AdmissionregistrationV1WebhookClientConfigDict,
        "failurePolicy": str,
        "matchPolicy": str,
        "name": str,
        "namespaceSelector": V1LabelSelectorDict,
        "objectSelector": V1LabelSelectorDict,
        "reinvocationPolicy": str,
        "rules": List[V1RuleWithOperationsDict],
        "sideEffects": str,
        "timeoutSeconds": int,
    },
    total=False,
)

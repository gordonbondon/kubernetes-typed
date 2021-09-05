# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1MutatingWebhookDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import AdmissionregistrationV1beta1WebhookClientConfigDict, V1LabelSelectorDict, V1beta1RuleWithOperationsDict

V1beta1MutatingWebhookDict = TypedDict(
    "V1beta1MutatingWebhookDict",
    {
        "admissionReviewVersions": List[str],
        "clientConfig": AdmissionregistrationV1beta1WebhookClientConfigDict,
        "failurePolicy": str,
        "matchPolicy": str,
        "name": str,
        "namespaceSelector": V1LabelSelectorDict,
        "objectSelector": V1LabelSelectorDict,
        "reinvocationPolicy": str,
        "rules": List[V1beta1RuleWithOperationsDict],
        "sideEffects": str,
        "timeoutSeconds": int,
    },
    total=False,
)

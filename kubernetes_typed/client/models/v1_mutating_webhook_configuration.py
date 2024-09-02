# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1MutatingWebhookConfigurationDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1_mutating_webhook import V1MutatingWebhookDict

V1MutatingWebhookConfigurationDict = TypedDict(
    "V1MutatingWebhookConfigurationDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "webhooks": List[V1MutatingWebhookDict],
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1MutatingWebhookConfigurationDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1MutatingWebhookDict, V1ObjectMetaDict

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

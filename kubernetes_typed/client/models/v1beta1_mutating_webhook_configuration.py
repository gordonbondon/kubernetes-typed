# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ObjectMetaDict, V1beta1MutatingWebhookDict

V1beta1MutatingWebhookConfigurationDict = TypedDict(
    "V1beta1MutatingWebhookConfigurationDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "webhooks": List[V1beta1MutatingWebhookDict],
    },
    total=False,
)

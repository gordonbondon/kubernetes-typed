# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1ObjectMetaDict, V1ValidatingWebhookDict

V1ValidatingWebhookConfigurationDict = TypedDict(
    "V1ValidatingWebhookConfigurationDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "webhooks": List[V1ValidatingWebhookDict],
    },
    total=False,
)
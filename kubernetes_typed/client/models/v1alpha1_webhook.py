# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1WebhookDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1alpha1WebhookClientConfigDict, V1alpha1WebhookThrottleConfigDict

V1alpha1WebhookDict = TypedDict(
    "V1alpha1WebhookDict",
    {
        "clientConfig": V1alpha1WebhookClientConfigDict,
        "throttle": V1alpha1WebhookThrottleConfigDict,
    },
    total=False,
)

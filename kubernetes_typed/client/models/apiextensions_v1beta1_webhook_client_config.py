# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import ApiextensionsV1beta1ServiceReferenceDict

ApiextensionsV1beta1WebhookClientConfigDict = TypedDict(
    "ApiextensionsV1beta1WebhookClientConfigDict",
    {
        "caBundle": str,
        "service": ApiextensionsV1beta1ServiceReferenceDict,
        "url": str,
    },
    total=False,
)
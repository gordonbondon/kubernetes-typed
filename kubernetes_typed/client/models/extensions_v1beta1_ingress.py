# Code generated by `typeddictgen`. DO NOT EDIT.
"""ExtensionsV1beta1IngressDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.extensions_v1beta1_ingress_spec import ExtensionsV1beta1IngressSpecDict
from kubernetes_typed.client.models.extensions_v1beta1_ingress_status import ExtensionsV1beta1IngressStatusDict

ExtensionsV1beta1IngressDict = TypedDict(
    "ExtensionsV1beta1IngressDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": ExtensionsV1beta1IngressSpecDict,
        "status": ExtensionsV1beta1IngressStatusDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""ExtensionsV1beta1IngressListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.extensions_v1beta1_ingress import ExtensionsV1beta1IngressDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

ExtensionsV1beta1IngressListDict = TypedDict(
    "ExtensionsV1beta1IngressListDict",
    {
        "apiVersion": str,
        "items": List[ExtensionsV1beta1IngressDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import ExtensionsV1beta1IngressDict, V1ListMetaDict

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
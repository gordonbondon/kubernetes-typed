# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import NetworkingV1beta1IngressDict, V1ListMetaDict

NetworkingV1beta1IngressListDict = TypedDict(
    "NetworkingV1beta1IngressListDict",
    {
        "apiVersion": str,
        "items": List[NetworkingV1beta1IngressDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1LoadBalancerStatusDict

ExtensionsV1beta1IngressStatusDict = TypedDict(
    "ExtensionsV1beta1IngressStatusDict",
    {
        "loadBalancer": V1LoadBalancerStatusDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""ExtensionsV1beta1IngressStatusDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_load_balancer_status import V1LoadBalancerStatusDict

ExtensionsV1beta1IngressStatusDict = TypedDict(
    "ExtensionsV1beta1IngressStatusDict",
    {
        "loadBalancer": V1LoadBalancerStatusDict,
    },
    total=False,
)

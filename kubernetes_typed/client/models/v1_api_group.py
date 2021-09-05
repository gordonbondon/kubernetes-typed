# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1APIGroupDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1GroupVersionForDiscoveryDict, V1ServerAddressByClientCIDRDict

V1APIGroupDict = TypedDict(
    "V1APIGroupDict",
    {
        "apiVersion": str,
        "kind": str,
        "name": str,
        "preferredVersion": V1GroupVersionForDiscoveryDict,
        "serverAddressByClientCIDRs": List[V1ServerAddressByClientCIDRDict],
        "versions": List[V1GroupVersionForDiscoveryDict],
    },
    total=False,
)

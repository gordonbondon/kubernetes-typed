# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1ObjectReferenceDict

V1EndpointAddressDict = TypedDict(
    "V1EndpointAddressDict",
    {
        "hostname": str,
        "ip": str,
        "nodeName": str,
        "targetRef": V1ObjectReferenceDict,
    },
    total=False,
)
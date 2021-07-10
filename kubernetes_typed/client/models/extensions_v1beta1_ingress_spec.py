# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import ExtensionsV1beta1IngressBackendDict, ExtensionsV1beta1IngressRuleDict, ExtensionsV1beta1IngressTLSDict

ExtensionsV1beta1IngressSpecDict = TypedDict(
    "ExtensionsV1beta1IngressSpecDict",
    {
        "backend": ExtensionsV1beta1IngressBackendDict,
        "rules": List[ExtensionsV1beta1IngressRuleDict],
        "tls": List[ExtensionsV1beta1IngressTLSDict],
    },
    total=False,
)
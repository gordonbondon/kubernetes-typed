# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import ExtensionsV1beta1HTTPIngressRuleValueDict

ExtensionsV1beta1IngressRuleDict = TypedDict(
    "ExtensionsV1beta1IngressRuleDict",
    {
        "host": str,
        "http": ExtensionsV1beta1HTTPIngressRuleValueDict,
    },
    total=False,
)
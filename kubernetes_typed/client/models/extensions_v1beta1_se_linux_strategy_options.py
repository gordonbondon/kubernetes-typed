# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1SELinuxOptionsDict

ExtensionsV1beta1SELinuxStrategyOptionsDict = TypedDict(
    "ExtensionsV1beta1SELinuxStrategyOptionsDict",
    {
        "rule": str,
        "seLinuxOptions": V1SELinuxOptionsDict,
    },
    total=False,
)
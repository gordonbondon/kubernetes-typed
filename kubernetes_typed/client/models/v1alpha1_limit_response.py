# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1alpha1QueuingConfigurationDict

V1alpha1LimitResponseDict = TypedDict(
    "V1alpha1LimitResponseDict",
    {
        "queuing": V1alpha1QueuingConfigurationDict,
        "type": str,
    },
    total=False,
)
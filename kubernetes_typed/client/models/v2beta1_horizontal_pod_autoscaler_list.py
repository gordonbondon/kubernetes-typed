# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List


from kubernetes_typed.client import V1ListMetaDict, V2beta1HorizontalPodAutoscalerDict

V2beta1HorizontalPodAutoscalerListDict = TypedDict(
    "V2beta1HorizontalPodAutoscalerListDict",
    {
        "apiVersion": str,
        "items": List[V2beta1HorizontalPodAutoscalerDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
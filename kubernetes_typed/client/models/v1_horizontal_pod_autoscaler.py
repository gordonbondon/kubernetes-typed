# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1HorizontalPodAutoscalerSpecDict, V1HorizontalPodAutoscalerStatusDict, V1ObjectMetaDict

V1HorizontalPodAutoscalerDict = TypedDict(
    "V1HorizontalPodAutoscalerDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1HorizontalPodAutoscalerSpecDict,
        "status": V1HorizontalPodAutoscalerStatusDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2HorizontalPodAutoscalerListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v2beta2_horizontal_pod_autoscaler import V2beta2HorizontalPodAutoscalerDict
from kubernetes_typed.client.models.v1_list_meta import V1ListMetaDict

V2beta2HorizontalPodAutoscalerListDict = TypedDict(
    "V2beta2HorizontalPodAutoscalerListDict",
    {
        "apiVersion": str,
        "items": List[V2beta2HorizontalPodAutoscalerDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)

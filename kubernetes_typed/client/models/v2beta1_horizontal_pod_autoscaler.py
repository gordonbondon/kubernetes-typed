# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta1HorizontalPodAutoscalerDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v2beta1_horizontal_pod_autoscaler_spec import V2beta1HorizontalPodAutoscalerSpecDict
from kubernetes_typed.client.models.v2beta1_horizontal_pod_autoscaler_status import V2beta1HorizontalPodAutoscalerStatusDict

V2beta1HorizontalPodAutoscalerDict = TypedDict(
    "V2beta1HorizontalPodAutoscalerDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V2beta1HorizontalPodAutoscalerSpecDict,
        "status": V2beta1HorizontalPodAutoscalerStatusDict,
    },
    total=False,
)

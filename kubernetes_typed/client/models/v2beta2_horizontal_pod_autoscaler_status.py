# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2HorizontalPodAutoscalerStatusDict generated type."""
import datetime
from typing import TypedDict, List

from kubernetes_typed.client.models.v2beta2_horizontal_pod_autoscaler_condition import V2beta2HorizontalPodAutoscalerConditionDict
from kubernetes_typed.client.models.v2beta2_metric_status import V2beta2MetricStatusDict

V2beta2HorizontalPodAutoscalerStatusDict = TypedDict(
    "V2beta2HorizontalPodAutoscalerStatusDict",
    {
        "conditions": List[V2beta2HorizontalPodAutoscalerConditionDict],
        "currentMetrics": List[V2beta2MetricStatusDict],
        "currentReplicas": int,
        "desiredReplicas": int,
        "lastScaleTime": datetime.datetime,
        "observedGeneration": int,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1EnvFromSourceDict, V1EnvVarDict, V1LabelSelectorDict, V1VolumeDict, V1VolumeMountDict

V1alpha1PodPresetSpecDict = TypedDict(
    "V1alpha1PodPresetSpecDict",
    {
        "env": List[V1EnvVarDict],
        "envFrom": List[V1EnvFromSourceDict],
        "selector": V1LabelSelectorDict,
        "volumeMounts": List[V1VolumeMountDict],
        "volumes": List[V1VolumeDict],
    },
    total=False,
)
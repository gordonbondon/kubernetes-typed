# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodTemplateSpecDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1PodSpecDict

V1PodTemplateSpecDict = TypedDict(
    "V1PodTemplateSpecDict",
    {
        "metadata": V1ObjectMetaDict,
        "spec": V1PodSpecDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict


from kubernetes_typed.client import V1LabelSelectorDict, V1PodTemplateSpecDict

V1beta1ReplicaSetSpecDict = TypedDict(
    "V1beta1ReplicaSetSpecDict",
    {
        "minReadySeconds": int,
        "replicas": int,
        "selector": V1LabelSelectorDict,
        "template": V1PodTemplateSpecDict,
    },
    total=False,
)
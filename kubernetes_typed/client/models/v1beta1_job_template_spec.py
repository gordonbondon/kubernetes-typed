# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1JobSpecDict, V1ObjectMetaDict

V1beta1JobTemplateSpecDict = TypedDict(
    "V1beta1JobTemplateSpecDict",
    {
        "metadata": V1ObjectMetaDict,
        "spec": V1JobSpecDict,
    },
    total=False,
)

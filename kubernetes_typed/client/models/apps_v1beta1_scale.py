# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import AppsV1beta1ScaleSpecDict, AppsV1beta1ScaleStatusDict, V1ObjectMetaDict

AppsV1beta1ScaleDict = TypedDict(
    "AppsV1beta1ScaleDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": AppsV1beta1ScaleSpecDict,
        "status": AppsV1beta1ScaleStatusDict,
    },
    total=False,
)

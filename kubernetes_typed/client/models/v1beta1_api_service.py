# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1APIServiceDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1beta1_api_service_spec import V1beta1APIServiceSpecDict
from kubernetes_typed.client.models.v1beta1_api_service_status import V1beta1APIServiceStatusDict

V1beta1APIServiceDict = TypedDict(
    "V1beta1APIServiceDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1APIServiceSpecDict,
        "status": V1beta1APIServiceStatusDict,
    },
    total=False,
)

# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ResourceQuotaDict generated type."""
from typing import TypedDict

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1_resource_quota_spec import V1ResourceQuotaSpecDict
from kubernetes_typed.client.models.v1_resource_quota_status import V1ResourceQuotaStatusDict

V1ResourceQuotaDict = TypedDict(
    "V1ResourceQuotaDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1ResourceQuotaSpecDict,
        "status": V1ResourceQuotaStatusDict,
    },
    total=False,
)

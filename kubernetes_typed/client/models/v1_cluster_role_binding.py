# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ClusterRoleBindingDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client.models.v1_object_meta import V1ObjectMetaDict
from kubernetes_typed.client.models.v1_role_ref import V1RoleRefDict
from kubernetes_typed.client.models.v1_subject import V1SubjectDict

V1ClusterRoleBindingDict = TypedDict(
    "V1ClusterRoleBindingDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "roleRef": V1RoleRefDict,
        "subjects": List[V1SubjectDict],
    },
    total=False,
)

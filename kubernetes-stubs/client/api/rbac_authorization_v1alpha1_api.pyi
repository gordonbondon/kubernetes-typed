# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any

class RbacAuthorizationV1alpha1Api:
    api_client: Any
    def __init__(self, api_client: Any | None = ...) -> None: ...
    def create_cluster_role(self, body, **kwargs): ...
    def create_cluster_role_with_http_info(self, body, **kwargs): ...
    def create_cluster_role_binding(self, body, **kwargs): ...
    def create_cluster_role_binding_with_http_info(self, body, **kwargs): ...
    def create_namespaced_role(self, namespace, body, **kwargs): ...
    def create_namespaced_role_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_role_binding(self, namespace, body, **kwargs): ...
    def create_namespaced_role_binding_with_http_info(self, namespace, body, **kwargs): ...
    def delete_cluster_role(self, name, **kwargs): ...
    def delete_cluster_role_with_http_info(self, name, **kwargs): ...
    def delete_cluster_role_binding(self, name, **kwargs): ...
    def delete_cluster_role_binding_with_http_info(self, name, **kwargs): ...
    def delete_collection_cluster_role(self, **kwargs): ...
    def delete_collection_cluster_role_with_http_info(self, **kwargs): ...
    def delete_collection_cluster_role_binding(self, **kwargs): ...
    def delete_collection_cluster_role_binding_with_http_info(self, **kwargs): ...
    def delete_collection_namespaced_role(self, namespace, **kwargs): ...
    def delete_collection_namespaced_role_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_role_binding(self, namespace, **kwargs): ...
    def delete_collection_namespaced_role_binding_with_http_info(self, namespace, **kwargs): ...
    def delete_namespaced_role(self, name, namespace, **kwargs): ...
    def delete_namespaced_role_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_role_binding(self, name, namespace, **kwargs): ...
    def delete_namespaced_role_binding_with_http_info(self, name, namespace, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_cluster_role(self, **kwargs): ...
    def list_cluster_role_with_http_info(self, **kwargs): ...
    def list_cluster_role_binding(self, **kwargs): ...
    def list_cluster_role_binding_with_http_info(self, **kwargs): ...
    def list_namespaced_role(self, namespace, **kwargs): ...
    def list_namespaced_role_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_role_binding(self, namespace, **kwargs): ...
    def list_namespaced_role_binding_with_http_info(self, namespace, **kwargs): ...
    def list_role_binding_for_all_namespaces(self, **kwargs): ...
    def list_role_binding_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_role_for_all_namespaces(self, **kwargs): ...
    def list_role_for_all_namespaces_with_http_info(self, **kwargs): ...
    def patch_cluster_role(self, name, body, **kwargs): ...
    def patch_cluster_role_with_http_info(self, name, body, **kwargs): ...
    def patch_cluster_role_binding(self, name, body, **kwargs): ...
    def patch_cluster_role_binding_with_http_info(self, name, body, **kwargs): ...
    def patch_namespaced_role(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_role_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_role_binding(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_role_binding_with_http_info(self, name, namespace, body, **kwargs): ...
    def read_cluster_role(self, name, **kwargs): ...
    def read_cluster_role_with_http_info(self, name, **kwargs): ...
    def read_cluster_role_binding(self, name, **kwargs): ...
    def read_cluster_role_binding_with_http_info(self, name, **kwargs): ...
    def read_namespaced_role(self, name, namespace, **kwargs): ...
    def read_namespaced_role_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_role_binding(self, name, namespace, **kwargs): ...
    def read_namespaced_role_binding_with_http_info(self, name, namespace, **kwargs): ...
    def replace_cluster_role(self, name, body, **kwargs): ...
    def replace_cluster_role_with_http_info(self, name, body, **kwargs): ...
    def replace_cluster_role_binding(self, name, body, **kwargs): ...
    def replace_cluster_role_binding_with_http_info(self, name, body, **kwargs): ...
    def replace_namespaced_role(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_role_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_role_binding(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_role_binding_with_http_info(self, name, namespace, body, **kwargs): ...

from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class CustomObjectsApi:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_cluster_custom_object(self, group: Any, version: Any, plural: Any, body: Any, **kwargs: Any): ...
    def create_cluster_custom_object_with_http_info(self, group: Any, version: Any, plural: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_custom_object(self, group: Any, version: Any, namespace: Any, plural: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_custom_object_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, body: Any, **kwargs: Any): ...
    def delete_cluster_custom_object(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def delete_cluster_custom_object_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def delete_collection_cluster_custom_object(self, group: Any, version: Any, plural: Any, **kwargs: Any): ...
    def delete_collection_cluster_custom_object_with_http_info(self, group: Any, version: Any, plural: Any, **kwargs: Any): ...
    def delete_collection_namespaced_custom_object(self, group: Any, version: Any, namespace: Any, plural: Any, **kwargs: Any): ...
    def delete_collection_namespaced_custom_object_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, **kwargs: Any): ...
    def delete_namespaced_custom_object(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def delete_namespaced_custom_object_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_cluster_custom_object(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_cluster_custom_object_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_cluster_custom_object_scale(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_cluster_custom_object_scale_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_cluster_custom_object_status(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_cluster_custom_object_status_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_namespaced_custom_object(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_namespaced_custom_object_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_namespaced_custom_object_scale(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_namespaced_custom_object_scale_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_namespaced_custom_object_status(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def get_namespaced_custom_object_status_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, **kwargs: Any): ...
    def list_cluster_custom_object(self, group: Any, version: Any, plural: Any, **kwargs: Any): ...
    def list_cluster_custom_object_with_http_info(self, group: Any, version: Any, plural: Any, **kwargs: Any): ...
    def list_namespaced_custom_object(self, group: Any, version: Any, namespace: Any, plural: Any, **kwargs: Any): ...
    def list_namespaced_custom_object_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, **kwargs: Any): ...
    def patch_cluster_custom_object(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_cluster_custom_object_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_cluster_custom_object_scale(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_cluster_custom_object_scale_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_cluster_custom_object_status(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_cluster_custom_object_status_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_custom_object(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_custom_object_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_custom_object_scale(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_custom_object_scale_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_custom_object_status(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_custom_object_status_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_cluster_custom_object(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_cluster_custom_object_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_cluster_custom_object_scale(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_cluster_custom_object_scale_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_cluster_custom_object_status(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_cluster_custom_object_status_with_http_info(self, group: Any, version: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_custom_object(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_custom_object_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_custom_object_scale(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_custom_object_scale_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_custom_object_status(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_custom_object_status_with_http_info(self, group: Any, version: Any, namespace: Any, plural: Any, name: Any, body: Any, **kwargs: Any): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any

class CoordinationV1Api:
    api_client: Any
    def __init__(self, api_client: Any | None = ...) -> None: ...
    def create_namespaced_lease(self, namespace, body, **kwargs): ...
    def create_namespaced_lease_with_http_info(self, namespace, body, **kwargs): ...
    def delete_collection_namespaced_lease(self, namespace, **kwargs): ...
    def delete_collection_namespaced_lease_with_http_info(self, namespace, **kwargs): ...
    def delete_namespaced_lease(self, name, namespace, **kwargs): ...
    def delete_namespaced_lease_with_http_info(self, name, namespace, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_lease_for_all_namespaces(self, **kwargs): ...
    def list_lease_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_namespaced_lease(self, namespace, **kwargs): ...
    def list_namespaced_lease_with_http_info(self, namespace, **kwargs): ...
    def patch_namespaced_lease(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_lease_with_http_info(self, name, namespace, body, **kwargs): ...
    def read_namespaced_lease(self, name, namespace, **kwargs): ...
    def read_namespaced_lease_with_http_info(self, name, namespace, **kwargs): ...
    def replace_namespaced_lease(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_lease_with_http_info(self, name, namespace, body, **kwargs): ...

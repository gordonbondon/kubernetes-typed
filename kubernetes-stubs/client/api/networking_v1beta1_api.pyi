# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any

class NetworkingV1beta1Api:
    api_client: Any
    def __init__(self, api_client: Any | None = ...) -> None: ...
    def create_ingress_class(self, body, **kwargs): ...
    def create_ingress_class_with_http_info(self, body, **kwargs): ...
    def create_namespaced_ingress(self, namespace, body, **kwargs): ...
    def create_namespaced_ingress_with_http_info(self, namespace, body, **kwargs): ...
    def delete_collection_ingress_class(self, **kwargs): ...
    def delete_collection_ingress_class_with_http_info(self, **kwargs): ...
    def delete_collection_namespaced_ingress(self, namespace, **kwargs): ...
    def delete_collection_namespaced_ingress_with_http_info(self, namespace, **kwargs): ...
    def delete_ingress_class(self, name, **kwargs): ...
    def delete_ingress_class_with_http_info(self, name, **kwargs): ...
    def delete_namespaced_ingress(self, name, namespace, **kwargs): ...
    def delete_namespaced_ingress_with_http_info(self, name, namespace, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_ingress_class(self, **kwargs): ...
    def list_ingress_class_with_http_info(self, **kwargs): ...
    def list_ingress_for_all_namespaces(self, **kwargs): ...
    def list_ingress_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_namespaced_ingress(self, namespace, **kwargs): ...
    def list_namespaced_ingress_with_http_info(self, namespace, **kwargs): ...
    def patch_ingress_class(self, name, body, **kwargs): ...
    def patch_ingress_class_with_http_info(self, name, body, **kwargs): ...
    def patch_namespaced_ingress(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_ingress_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_ingress_status(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_ingress_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def read_ingress_class(self, name, **kwargs): ...
    def read_ingress_class_with_http_info(self, name, **kwargs): ...
    def read_namespaced_ingress(self, name, namespace, **kwargs): ...
    def read_namespaced_ingress_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_ingress_status(self, name, namespace, **kwargs): ...
    def read_namespaced_ingress_status_with_http_info(self, name, namespace, **kwargs): ...
    def replace_ingress_class(self, name, body, **kwargs): ...
    def replace_ingress_class_with_http_info(self, name, body, **kwargs): ...
    def replace_namespaced_ingress(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_ingress_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_ingress_status(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_ingress_status_with_http_info(self, name, namespace, body, **kwargs): ...

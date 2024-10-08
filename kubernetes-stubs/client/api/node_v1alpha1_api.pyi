# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError

class NodeV1alpha1Api:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def create_runtime_class(self, body, **kwargs): ...
    def create_runtime_class_with_http_info(self, body, **kwargs): ...
    def delete_collection_runtime_class(self, **kwargs): ...
    def delete_collection_runtime_class_with_http_info(self, **kwargs): ...
    def delete_runtime_class(self, name, **kwargs): ...
    def delete_runtime_class_with_http_info(self, name, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_runtime_class(self, **kwargs): ...
    def list_runtime_class_with_http_info(self, **kwargs): ...
    def patch_runtime_class(self, name, body, **kwargs): ...
    def patch_runtime_class_with_http_info(self, name, body, **kwargs): ...
    def read_runtime_class(self, name, **kwargs): ...
    def read_runtime_class_with_http_info(self, name, **kwargs): ...
    def replace_runtime_class(self, name, body, **kwargs): ...
    def replace_runtime_class_with_http_info(self, name, body, **kwargs): ...

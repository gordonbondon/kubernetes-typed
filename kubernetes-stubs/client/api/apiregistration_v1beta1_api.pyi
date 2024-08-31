# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError

class ApiregistrationV1beta1Api:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def create_api_service(self, body, **kwargs): ...
    def create_api_service_with_http_info(self, body, **kwargs): ...
    def delete_api_service(self, name, **kwargs): ...
    def delete_api_service_with_http_info(self, name, **kwargs): ...
    def delete_collection_api_service(self, **kwargs): ...
    def delete_collection_api_service_with_http_info(self, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_api_service(self, **kwargs): ...
    def list_api_service_with_http_info(self, **kwargs): ...
    def patch_api_service(self, name, body, **kwargs): ...
    def patch_api_service_with_http_info(self, name, body, **kwargs): ...
    def patch_api_service_status(self, name, body, **kwargs): ...
    def patch_api_service_status_with_http_info(self, name, body, **kwargs): ...
    def read_api_service(self, name, **kwargs): ...
    def read_api_service_with_http_info(self, name, **kwargs): ...
    def read_api_service_status(self, name, **kwargs): ...
    def read_api_service_status_with_http_info(self, name, **kwargs): ...
    def replace_api_service(self, name, body, **kwargs): ...
    def replace_api_service_with_http_info(self, name, body, **kwargs): ...
    def replace_api_service_status(self, name, body, **kwargs): ...
    def replace_api_service_status_with_http_info(self, name, body, **kwargs): ...

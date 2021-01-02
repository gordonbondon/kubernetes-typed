from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class ApiregistrationV1beta1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_api_service(self, body: Any, **kwargs: Any): ...
    def create_api_service_with_http_info(self, body: Any, **kwargs: Any): ...
    def delete_api_service(self, name: Any, **kwargs: Any): ...
    def delete_api_service_with_http_info(self, name: Any, **kwargs: Any): ...
    def delete_collection_api_service(self, **kwargs: Any): ...
    def delete_collection_api_service_with_http_info(self, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_api_service(self, **kwargs: Any): ...
    def list_api_service_with_http_info(self, **kwargs: Any): ...
    def patch_api_service(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_api_service_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_api_service_status(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_api_service_status_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def read_api_service(self, name: Any, **kwargs: Any): ...
    def read_api_service_with_http_info(self, name: Any, **kwargs: Any): ...
    def read_api_service_status(self, name: Any, **kwargs: Any): ...
    def read_api_service_status_with_http_info(self, name: Any, **kwargs: Any): ...
    def replace_api_service(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_api_service_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_api_service_status(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_api_service_status_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...

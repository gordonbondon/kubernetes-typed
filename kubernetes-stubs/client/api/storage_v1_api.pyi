# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class StorageV1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_storage_class(self, body: Any, **kwargs: Any): ...
    def create_storage_class_with_http_info(self, body: Any, **kwargs: Any): ...
    def create_volume_attachment(self, body: Any, **kwargs: Any): ...
    def create_volume_attachment_with_http_info(self, body: Any, **kwargs: Any): ...
    def delete_collection_storage_class(self, **kwargs: Any): ...
    def delete_collection_storage_class_with_http_info(self, **kwargs: Any): ...
    def delete_collection_volume_attachment(self, **kwargs: Any): ...
    def delete_collection_volume_attachment_with_http_info(self, **kwargs: Any): ...
    def delete_storage_class(self, name: Any, **kwargs: Any): ...
    def delete_storage_class_with_http_info(self, name: Any, **kwargs: Any): ...
    def delete_volume_attachment(self, name: Any, **kwargs: Any): ...
    def delete_volume_attachment_with_http_info(self, name: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_storage_class(self, **kwargs: Any): ...
    def list_storage_class_with_http_info(self, **kwargs: Any): ...
    def list_volume_attachment(self, **kwargs: Any): ...
    def list_volume_attachment_with_http_info(self, **kwargs: Any): ...
    def patch_storage_class(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_storage_class_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_volume_attachment(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_volume_attachment_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_volume_attachment_status(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_volume_attachment_status_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def read_storage_class(self, name: Any, **kwargs: Any): ...
    def read_storage_class_with_http_info(self, name: Any, **kwargs: Any): ...
    def read_volume_attachment(self, name: Any, **kwargs: Any): ...
    def read_volume_attachment_with_http_info(self, name: Any, **kwargs: Any): ...
    def read_volume_attachment_status(self, name: Any, **kwargs: Any): ...
    def read_volume_attachment_status_with_http_info(self, name: Any, **kwargs: Any): ...
    def replace_storage_class(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_storage_class_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_volume_attachment(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_volume_attachment_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_volume_attachment_status(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_volume_attachment_status_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...

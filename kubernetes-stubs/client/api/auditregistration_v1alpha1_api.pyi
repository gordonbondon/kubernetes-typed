# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class AuditregistrationV1alpha1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_audit_sink(self, body: Any, **kwargs: Any): ...
    def create_audit_sink_with_http_info(self, body: Any, **kwargs: Any): ...
    def delete_audit_sink(self, name: Any, **kwargs: Any): ...
    def delete_audit_sink_with_http_info(self, name: Any, **kwargs: Any): ...
    def delete_collection_audit_sink(self, **kwargs: Any): ...
    def delete_collection_audit_sink_with_http_info(self, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_audit_sink(self, **kwargs: Any): ...
    def list_audit_sink_with_http_info(self, **kwargs: Any): ...
    def patch_audit_sink(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_audit_sink_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def read_audit_sink(self, name: Any, **kwargs: Any): ...
    def read_audit_sink_with_http_info(self, name: Any, **kwargs: Any): ...
    def replace_audit_sink(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_audit_sink_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...

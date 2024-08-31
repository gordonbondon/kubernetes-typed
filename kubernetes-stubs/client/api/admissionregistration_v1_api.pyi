# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError

class AdmissionregistrationV1Api:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def create_mutating_webhook_configuration(self, body, **kwargs): ...
    def create_mutating_webhook_configuration_with_http_info(self, body, **kwargs): ...
    def create_validating_webhook_configuration(self, body, **kwargs): ...
    def create_validating_webhook_configuration_with_http_info(self, body, **kwargs): ...
    def delete_collection_mutating_webhook_configuration(self, **kwargs): ...
    def delete_collection_mutating_webhook_configuration_with_http_info(self, **kwargs): ...
    def delete_collection_validating_webhook_configuration(self, **kwargs): ...
    def delete_collection_validating_webhook_configuration_with_http_info(self, **kwargs): ...
    def delete_mutating_webhook_configuration(self, name, **kwargs): ...
    def delete_mutating_webhook_configuration_with_http_info(self, name, **kwargs): ...
    def delete_validating_webhook_configuration(self, name, **kwargs): ...
    def delete_validating_webhook_configuration_with_http_info(self, name, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_mutating_webhook_configuration(self, **kwargs): ...
    def list_mutating_webhook_configuration_with_http_info(self, **kwargs): ...
    def list_validating_webhook_configuration(self, **kwargs): ...
    def list_validating_webhook_configuration_with_http_info(self, **kwargs): ...
    def patch_mutating_webhook_configuration(self, name, body, **kwargs): ...
    def patch_mutating_webhook_configuration_with_http_info(self, name, body, **kwargs): ...
    def patch_validating_webhook_configuration(self, name, body, **kwargs): ...
    def patch_validating_webhook_configuration_with_http_info(self, name, body, **kwargs): ...
    def read_mutating_webhook_configuration(self, name, **kwargs): ...
    def read_mutating_webhook_configuration_with_http_info(self, name, **kwargs): ...
    def read_validating_webhook_configuration(self, name, **kwargs): ...
    def read_validating_webhook_configuration_with_http_info(self, name, **kwargs): ...
    def replace_mutating_webhook_configuration(self, name, body, **kwargs): ...
    def replace_mutating_webhook_configuration_with_http_info(self, name, body, **kwargs): ...
    def replace_validating_webhook_configuration(self, name, body, **kwargs): ...
    def replace_validating_webhook_configuration_with_http_info(self, name, body, **kwargs): ...

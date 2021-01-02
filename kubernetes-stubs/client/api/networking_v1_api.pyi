from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class NetworkingV1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_namespaced_network_policy(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_network_policy_with_http_info(self, namespace: Any, body: Any, **kwargs: Any): ...
    def delete_collection_namespaced_network_policy(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_namespaced_network_policy_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_network_policy(self, name: Any, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_namespaced_network_policy(self, namespace: Any, **kwargs: Any): ...
    def list_namespaced_network_policy_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def list_network_policy_for_all_namespaces(self, **kwargs: Any): ...
    def list_network_policy_for_all_namespaces_with_http_info(self, **kwargs: Any): ...
    def patch_namespaced_network_policy(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def read_namespaced_network_policy(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def replace_namespaced_network_policy(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...

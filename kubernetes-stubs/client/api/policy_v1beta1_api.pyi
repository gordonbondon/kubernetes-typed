from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class PolicyV1beta1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_namespaced_pod_disruption_budget(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_pod_disruption_budget_with_http_info(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_pod_security_policy(self, body: Any, **kwargs: Any): ...
    def create_pod_security_policy_with_http_info(self, body: Any, **kwargs: Any): ...
    def delete_collection_namespaced_pod_disruption_budget(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_namespaced_pod_disruption_budget_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_pod_security_policy(self, **kwargs: Any): ...
    def delete_collection_pod_security_policy_with_http_info(self, **kwargs: Any): ...
    def delete_namespaced_pod_disruption_budget(self, name: Any, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_pod_disruption_budget_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def delete_pod_security_policy(self, name: Any, **kwargs: Any): ...
    def delete_pod_security_policy_with_http_info(self, name: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_namespaced_pod_disruption_budget(self, namespace: Any, **kwargs: Any): ...
    def list_namespaced_pod_disruption_budget_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def list_pod_disruption_budget_for_all_namespaces(self, **kwargs: Any): ...
    def list_pod_disruption_budget_for_all_namespaces_with_http_info(self, **kwargs: Any): ...
    def list_pod_security_policy(self, **kwargs: Any): ...
    def list_pod_security_policy_with_http_info(self, **kwargs: Any): ...
    def patch_namespaced_pod_disruption_budget(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_pod_disruption_budget_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_pod_disruption_budget_status(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_pod_disruption_budget_status_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_pod_security_policy(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_pod_security_policy_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def read_namespaced_pod_disruption_budget(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_pod_disruption_budget_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_pod_disruption_budget_status(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_pod_disruption_budget_status_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_pod_security_policy(self, name: Any, **kwargs: Any): ...
    def read_pod_security_policy_with_http_info(self, name: Any, **kwargs: Any): ...
    def replace_namespaced_pod_disruption_budget(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_pod_disruption_budget_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_pod_disruption_budget_status(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_pod_disruption_budget_status_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_pod_security_policy(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_pod_security_policy_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...

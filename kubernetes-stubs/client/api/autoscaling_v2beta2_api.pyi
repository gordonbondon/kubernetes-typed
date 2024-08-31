# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError

class AutoscalingV2beta2Api:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def create_namespaced_horizontal_pod_autoscaler(self, namespace, body, **kwargs): ...
    def create_namespaced_horizontal_pod_autoscaler_with_http_info(self, namespace, body, **kwargs): ...
    def delete_collection_namespaced_horizontal_pod_autoscaler(self, namespace, **kwargs): ...
    def delete_collection_namespaced_horizontal_pod_autoscaler_with_http_info(self, namespace, **kwargs): ...
    def delete_namespaced_horizontal_pod_autoscaler(self, name, namespace, **kwargs): ...
    def delete_namespaced_horizontal_pod_autoscaler_with_http_info(self, name, namespace, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_horizontal_pod_autoscaler_for_all_namespaces(self, **kwargs): ...
    def list_horizontal_pod_autoscaler_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_namespaced_horizontal_pod_autoscaler(self, namespace, **kwargs): ...
    def list_namespaced_horizontal_pod_autoscaler_with_http_info(self, namespace, **kwargs): ...
    def patch_namespaced_horizontal_pod_autoscaler(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_horizontal_pod_autoscaler_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_horizontal_pod_autoscaler_status(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_horizontal_pod_autoscaler_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def read_namespaced_horizontal_pod_autoscaler(self, name, namespace, **kwargs): ...
    def read_namespaced_horizontal_pod_autoscaler_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_horizontal_pod_autoscaler_status(self, name, namespace, **kwargs): ...
    def read_namespaced_horizontal_pod_autoscaler_status_with_http_info(self, name, namespace, **kwargs): ...
    def replace_namespaced_horizontal_pod_autoscaler(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_horizontal_pod_autoscaler_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_horizontal_pod_autoscaler_status(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_horizontal_pod_autoscaler_status_with_http_info(self, name, namespace, body, **kwargs): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError

class CoreV1Api:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def connect_delete_namespaced_pod_proxy(self, name, namespace, **kwargs): ...
    def connect_delete_namespaced_pod_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_delete_namespaced_pod_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_delete_namespaced_pod_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_delete_namespaced_service_proxy(self, name, namespace, **kwargs): ...
    def connect_delete_namespaced_service_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_delete_namespaced_service_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_delete_namespaced_service_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_delete_node_proxy(self, name, **kwargs): ...
    def connect_delete_node_proxy_with_http_info(self, name, **kwargs): ...
    def connect_delete_node_proxy_with_path(self, name, path, **kwargs): ...
    def connect_delete_node_proxy_with_path_with_http_info(self, name, path, **kwargs): ...
    def connect_get_namespaced_pod_attach(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_attach_with_http_info(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_exec(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_exec_with_http_info(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_portforward(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_portforward_with_http_info(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_proxy(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_pod_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_get_namespaced_pod_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_get_namespaced_service_proxy(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_service_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_get_namespaced_service_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_get_namespaced_service_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_get_node_proxy(self, name, **kwargs): ...
    def connect_get_node_proxy_with_http_info(self, name, **kwargs): ...
    def connect_get_node_proxy_with_path(self, name, path, **kwargs): ...
    def connect_get_node_proxy_with_path_with_http_info(self, name, path, **kwargs): ...
    def connect_head_namespaced_pod_proxy(self, name, namespace, **kwargs): ...
    def connect_head_namespaced_pod_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_head_namespaced_pod_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_head_namespaced_pod_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_head_namespaced_service_proxy(self, name, namespace, **kwargs): ...
    def connect_head_namespaced_service_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_head_namespaced_service_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_head_namespaced_service_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_head_node_proxy(self, name, **kwargs): ...
    def connect_head_node_proxy_with_http_info(self, name, **kwargs): ...
    def connect_head_node_proxy_with_path(self, name, path, **kwargs): ...
    def connect_head_node_proxy_with_path_with_http_info(self, name, path, **kwargs): ...
    def connect_options_namespaced_pod_proxy(self, name, namespace, **kwargs): ...
    def connect_options_namespaced_pod_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_options_namespaced_pod_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_options_namespaced_pod_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_options_namespaced_service_proxy(self, name, namespace, **kwargs): ...
    def connect_options_namespaced_service_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_options_namespaced_service_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_options_namespaced_service_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_options_node_proxy(self, name, **kwargs): ...
    def connect_options_node_proxy_with_http_info(self, name, **kwargs): ...
    def connect_options_node_proxy_with_path(self, name, path, **kwargs): ...
    def connect_options_node_proxy_with_path_with_http_info(self, name, path, **kwargs): ...
    def connect_patch_namespaced_pod_proxy(self, name, namespace, **kwargs): ...
    def connect_patch_namespaced_pod_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_patch_namespaced_pod_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_patch_namespaced_pod_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_patch_namespaced_service_proxy(self, name, namespace, **kwargs): ...
    def connect_patch_namespaced_service_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_patch_namespaced_service_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_patch_namespaced_service_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_patch_node_proxy(self, name, **kwargs): ...
    def connect_patch_node_proxy_with_http_info(self, name, **kwargs): ...
    def connect_patch_node_proxy_with_path(self, name, path, **kwargs): ...
    def connect_patch_node_proxy_with_path_with_http_info(self, name, path, **kwargs): ...
    def connect_post_namespaced_pod_attach(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_attach_with_http_info(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_exec(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_exec_with_http_info(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_portforward(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_portforward_with_http_info(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_proxy(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_pod_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_post_namespaced_pod_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_post_namespaced_service_proxy(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_service_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_post_namespaced_service_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_post_namespaced_service_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_post_node_proxy(self, name, **kwargs): ...
    def connect_post_node_proxy_with_http_info(self, name, **kwargs): ...
    def connect_post_node_proxy_with_path(self, name, path, **kwargs): ...
    def connect_post_node_proxy_with_path_with_http_info(self, name, path, **kwargs): ...
    def connect_put_namespaced_pod_proxy(self, name, namespace, **kwargs): ...
    def connect_put_namespaced_pod_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_put_namespaced_pod_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_put_namespaced_pod_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_put_namespaced_service_proxy(self, name, namespace, **kwargs): ...
    def connect_put_namespaced_service_proxy_with_http_info(self, name, namespace, **kwargs): ...
    def connect_put_namespaced_service_proxy_with_path(self, name, namespace, path, **kwargs): ...
    def connect_put_namespaced_service_proxy_with_path_with_http_info(self, name, namespace, path, **kwargs): ...
    def connect_put_node_proxy(self, name, **kwargs): ...
    def connect_put_node_proxy_with_http_info(self, name, **kwargs): ...
    def connect_put_node_proxy_with_path(self, name, path, **kwargs): ...
    def connect_put_node_proxy_with_path_with_http_info(self, name, path, **kwargs): ...
    def create_namespace(self, body, **kwargs): ...
    def create_namespace_with_http_info(self, body, **kwargs): ...
    def create_namespaced_binding(self, namespace, body, **kwargs): ...
    def create_namespaced_binding_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_config_map(self, namespace, body, **kwargs): ...
    def create_namespaced_config_map_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_endpoints(self, namespace, body, **kwargs): ...
    def create_namespaced_endpoints_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_event(self, namespace, body, **kwargs): ...
    def create_namespaced_event_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_limit_range(self, namespace, body, **kwargs): ...
    def create_namespaced_limit_range_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_persistent_volume_claim(self, namespace, body, **kwargs): ...
    def create_namespaced_persistent_volume_claim_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_pod(self, namespace, body, **kwargs): ...
    def create_namespaced_pod_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_pod_binding(self, name, namespace, body, **kwargs): ...
    def create_namespaced_pod_binding_with_http_info(self, name, namespace, body, **kwargs): ...
    def create_namespaced_pod_eviction(self, name, namespace, body, **kwargs): ...
    def create_namespaced_pod_eviction_with_http_info(self, name, namespace, body, **kwargs): ...
    def create_namespaced_pod_template(self, namespace, body, **kwargs): ...
    def create_namespaced_pod_template_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_replication_controller(self, namespace, body, **kwargs): ...
    def create_namespaced_replication_controller_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_resource_quota(self, namespace, body, **kwargs): ...
    def create_namespaced_resource_quota_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_secret(self, namespace, body, **kwargs): ...
    def create_namespaced_secret_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_service(self, namespace, body, **kwargs): ...
    def create_namespaced_service_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_service_account(self, namespace, body, **kwargs): ...
    def create_namespaced_service_account_with_http_info(self, namespace, body, **kwargs): ...
    def create_namespaced_service_account_token(self, name, namespace, body, **kwargs): ...
    def create_namespaced_service_account_token_with_http_info(self, name, namespace, body, **kwargs): ...
    def create_node(self, body, **kwargs): ...
    def create_node_with_http_info(self, body, **kwargs): ...
    def create_persistent_volume(self, body, **kwargs): ...
    def create_persistent_volume_with_http_info(self, body, **kwargs): ...
    def delete_collection_namespaced_config_map(self, namespace, **kwargs): ...
    def delete_collection_namespaced_config_map_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_endpoints(self, namespace, **kwargs): ...
    def delete_collection_namespaced_endpoints_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_event(self, namespace, **kwargs): ...
    def delete_collection_namespaced_event_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_limit_range(self, namespace, **kwargs): ...
    def delete_collection_namespaced_limit_range_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_persistent_volume_claim(self, namespace, **kwargs): ...
    def delete_collection_namespaced_persistent_volume_claim_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_pod(self, namespace, **kwargs): ...
    def delete_collection_namespaced_pod_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_pod_template(self, namespace, **kwargs): ...
    def delete_collection_namespaced_pod_template_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_replication_controller(self, namespace, **kwargs): ...
    def delete_collection_namespaced_replication_controller_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_resource_quota(self, namespace, **kwargs): ...
    def delete_collection_namespaced_resource_quota_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_secret(self, namespace, **kwargs): ...
    def delete_collection_namespaced_secret_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_namespaced_service_account(self, namespace, **kwargs): ...
    def delete_collection_namespaced_service_account_with_http_info(self, namespace, **kwargs): ...
    def delete_collection_node(self, **kwargs): ...
    def delete_collection_node_with_http_info(self, **kwargs): ...
    def delete_collection_persistent_volume(self, **kwargs): ...
    def delete_collection_persistent_volume_with_http_info(self, **kwargs): ...
    def delete_namespace(self, name, **kwargs): ...
    def delete_namespace_with_http_info(self, name, **kwargs): ...
    def delete_namespaced_config_map(self, name, namespace, **kwargs): ...
    def delete_namespaced_config_map_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_endpoints(self, name, namespace, **kwargs): ...
    def delete_namespaced_endpoints_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_event(self, name, namespace, **kwargs): ...
    def delete_namespaced_event_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_limit_range(self, name, namespace, **kwargs): ...
    def delete_namespaced_limit_range_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_persistent_volume_claim(self, name, namespace, **kwargs): ...
    def delete_namespaced_persistent_volume_claim_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_pod(self, name, namespace, **kwargs): ...
    def delete_namespaced_pod_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_pod_template(self, name, namespace, **kwargs): ...
    def delete_namespaced_pod_template_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_replication_controller(self, name, namespace, **kwargs): ...
    def delete_namespaced_replication_controller_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_resource_quota(self, name, namespace, **kwargs): ...
    def delete_namespaced_resource_quota_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_secret(self, name, namespace, **kwargs): ...
    def delete_namespaced_secret_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_service(self, name, namespace, **kwargs): ...
    def delete_namespaced_service_with_http_info(self, name, namespace, **kwargs): ...
    def delete_namespaced_service_account(self, name, namespace, **kwargs): ...
    def delete_namespaced_service_account_with_http_info(self, name, namespace, **kwargs): ...
    def delete_node(self, name, **kwargs): ...
    def delete_node_with_http_info(self, name, **kwargs): ...
    def delete_persistent_volume(self, name, **kwargs): ...
    def delete_persistent_volume_with_http_info(self, name, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_component_status(self, **kwargs): ...
    def list_component_status_with_http_info(self, **kwargs): ...
    def list_config_map_for_all_namespaces(self, **kwargs): ...
    def list_config_map_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_endpoints_for_all_namespaces(self, **kwargs): ...
    def list_endpoints_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_event_for_all_namespaces(self, **kwargs): ...
    def list_event_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_limit_range_for_all_namespaces(self, **kwargs): ...
    def list_limit_range_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_namespace(self, **kwargs): ...
    def list_namespace_with_http_info(self, **kwargs): ...
    def list_namespaced_config_map(self, namespace, **kwargs): ...
    def list_namespaced_config_map_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_endpoints(self, namespace, **kwargs): ...
    def list_namespaced_endpoints_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_event(self, namespace, **kwargs): ...
    def list_namespaced_event_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_limit_range(self, namespace, **kwargs): ...
    def list_namespaced_limit_range_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_persistent_volume_claim(self, namespace, **kwargs): ...
    def list_namespaced_persistent_volume_claim_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_pod(self, namespace, **kwargs): ...
    def list_namespaced_pod_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_pod_template(self, namespace, **kwargs): ...
    def list_namespaced_pod_template_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_replication_controller(self, namespace, **kwargs): ...
    def list_namespaced_replication_controller_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_resource_quota(self, namespace, **kwargs): ...
    def list_namespaced_resource_quota_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_secret(self, namespace, **kwargs): ...
    def list_namespaced_secret_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_service(self, namespace, **kwargs): ...
    def list_namespaced_service_with_http_info(self, namespace, **kwargs): ...
    def list_namespaced_service_account(self, namespace, **kwargs): ...
    def list_namespaced_service_account_with_http_info(self, namespace, **kwargs): ...
    def list_node(self, **kwargs): ...
    def list_node_with_http_info(self, **kwargs): ...
    def list_persistent_volume(self, **kwargs): ...
    def list_persistent_volume_with_http_info(self, **kwargs): ...
    def list_persistent_volume_claim_for_all_namespaces(self, **kwargs): ...
    def list_persistent_volume_claim_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_pod_for_all_namespaces(self, **kwargs): ...
    def list_pod_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_pod_template_for_all_namespaces(self, **kwargs): ...
    def list_pod_template_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_replication_controller_for_all_namespaces(self, **kwargs): ...
    def list_replication_controller_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_resource_quota_for_all_namespaces(self, **kwargs): ...
    def list_resource_quota_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_secret_for_all_namespaces(self, **kwargs): ...
    def list_secret_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_service_account_for_all_namespaces(self, **kwargs): ...
    def list_service_account_for_all_namespaces_with_http_info(self, **kwargs): ...
    def list_service_for_all_namespaces(self, **kwargs): ...
    def list_service_for_all_namespaces_with_http_info(self, **kwargs): ...
    def patch_namespace(self, name, body, **kwargs): ...
    def patch_namespace_with_http_info(self, name, body, **kwargs): ...
    def patch_namespace_status(self, name, body, **kwargs): ...
    def patch_namespace_status_with_http_info(self, name, body, **kwargs): ...
    def patch_namespaced_config_map(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_config_map_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_endpoints(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_endpoints_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_event(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_event_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_limit_range(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_limit_range_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_persistent_volume_claim(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_persistent_volume_claim_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_persistent_volume_claim_status(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_persistent_volume_claim_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_pod(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_pod_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_pod_status(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_pod_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_pod_template(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_pod_template_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_replication_controller(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_replication_controller_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_replication_controller_scale(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_replication_controller_scale_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_replication_controller_status(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_replication_controller_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_resource_quota(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_resource_quota_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_resource_quota_status(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_resource_quota_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_secret(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_secret_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_service(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_service_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_service_account(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_service_account_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_service_status(self, name, namespace, body, **kwargs): ...
    def patch_namespaced_service_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def patch_node(self, name, body, **kwargs): ...
    def patch_node_with_http_info(self, name, body, **kwargs): ...
    def patch_node_status(self, name, body, **kwargs): ...
    def patch_node_status_with_http_info(self, name, body, **kwargs): ...
    def patch_persistent_volume(self, name, body, **kwargs): ...
    def patch_persistent_volume_with_http_info(self, name, body, **kwargs): ...
    def patch_persistent_volume_status(self, name, body, **kwargs): ...
    def patch_persistent_volume_status_with_http_info(self, name, body, **kwargs): ...
    def read_component_status(self, name, **kwargs): ...
    def read_component_status_with_http_info(self, name, **kwargs): ...
    def read_namespace(self, name, **kwargs): ...
    def read_namespace_with_http_info(self, name, **kwargs): ...
    def read_namespace_status(self, name, **kwargs): ...
    def read_namespace_status_with_http_info(self, name, **kwargs): ...
    def read_namespaced_config_map(self, name, namespace, **kwargs): ...
    def read_namespaced_config_map_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_endpoints(self, name, namespace, **kwargs): ...
    def read_namespaced_endpoints_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_event(self, name, namespace, **kwargs): ...
    def read_namespaced_event_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_limit_range(self, name, namespace, **kwargs): ...
    def read_namespaced_limit_range_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_persistent_volume_claim(self, name, namespace, **kwargs): ...
    def read_namespaced_persistent_volume_claim_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_persistent_volume_claim_status(self, name, namespace, **kwargs): ...
    def read_namespaced_persistent_volume_claim_status_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_pod(self, name, namespace, **kwargs): ...
    def read_namespaced_pod_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_pod_log(self, name, namespace, **kwargs): ...
    def read_namespaced_pod_log_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_pod_status(self, name, namespace, **kwargs): ...
    def read_namespaced_pod_status_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_pod_template(self, name, namespace, **kwargs): ...
    def read_namespaced_pod_template_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_replication_controller(self, name, namespace, **kwargs): ...
    def read_namespaced_replication_controller_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_replication_controller_scale(self, name, namespace, **kwargs): ...
    def read_namespaced_replication_controller_scale_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_replication_controller_status(self, name, namespace, **kwargs): ...
    def read_namespaced_replication_controller_status_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_resource_quota(self, name, namespace, **kwargs): ...
    def read_namespaced_resource_quota_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_resource_quota_status(self, name, namespace, **kwargs): ...
    def read_namespaced_resource_quota_status_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_secret(self, name, namespace, **kwargs): ...
    def read_namespaced_secret_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_service(self, name, namespace, **kwargs): ...
    def read_namespaced_service_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_service_account(self, name, namespace, **kwargs): ...
    def read_namespaced_service_account_with_http_info(self, name, namespace, **kwargs): ...
    def read_namespaced_service_status(self, name, namespace, **kwargs): ...
    def read_namespaced_service_status_with_http_info(self, name, namespace, **kwargs): ...
    def read_node(self, name, **kwargs): ...
    def read_node_with_http_info(self, name, **kwargs): ...
    def read_node_status(self, name, **kwargs): ...
    def read_node_status_with_http_info(self, name, **kwargs): ...
    def read_persistent_volume(self, name, **kwargs): ...
    def read_persistent_volume_with_http_info(self, name, **kwargs): ...
    def read_persistent_volume_status(self, name, **kwargs): ...
    def read_persistent_volume_status_with_http_info(self, name, **kwargs): ...
    def replace_namespace(self, name, body, **kwargs): ...
    def replace_namespace_with_http_info(self, name, body, **kwargs): ...
    def replace_namespace_finalize(self, name, body, **kwargs): ...
    def replace_namespace_finalize_with_http_info(self, name, body, **kwargs): ...
    def replace_namespace_status(self, name, body, **kwargs): ...
    def replace_namespace_status_with_http_info(self, name, body, **kwargs): ...
    def replace_namespaced_config_map(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_config_map_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_endpoints(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_endpoints_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_event(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_event_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_limit_range(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_limit_range_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_persistent_volume_claim(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_persistent_volume_claim_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_persistent_volume_claim_status(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_persistent_volume_claim_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_pod(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_pod_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_pod_status(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_pod_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_pod_template(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_pod_template_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_replication_controller(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_replication_controller_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_replication_controller_scale(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_replication_controller_scale_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_replication_controller_status(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_replication_controller_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_resource_quota(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_resource_quota_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_resource_quota_status(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_resource_quota_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_secret(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_secret_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_service(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_service_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_service_account(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_service_account_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_service_status(self, name, namespace, body, **kwargs): ...
    def replace_namespaced_service_status_with_http_info(self, name, namespace, body, **kwargs): ...
    def replace_node(self, name, body, **kwargs): ...
    def replace_node_with_http_info(self, name, body, **kwargs): ...
    def replace_node_status(self, name, body, **kwargs): ...
    def replace_node_status_with_http_info(self, name, body, **kwargs): ...
    def replace_persistent_volume(self, name, body, **kwargs): ...
    def replace_persistent_volume_with_http_info(self, name, body, **kwargs): ...
    def replace_persistent_volume_status(self, name, body, **kwargs): ...
    def replace_persistent_volume_status_with_http_info(self, name, body, **kwargs): ...

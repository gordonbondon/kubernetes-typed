# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ServiceSpec:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, cluster_ip: Incomplete | None = None, external_i_ps: Incomplete | None = None, external_name: Incomplete | None = None, external_traffic_policy: Incomplete | None = None, health_check_node_port: Incomplete | None = None, ip_family: Incomplete | None = None, load_balancer_ip: Incomplete | None = None, load_balancer_source_ranges: Incomplete | None = None, ports: Incomplete | None = None, publish_not_ready_addresses: Incomplete | None = None, selector: Incomplete | None = None, session_affinity: Incomplete | None = None, session_affinity_config: Incomplete | None = None, topology_keys: Incomplete | None = None, type: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def cluster_ip(self): ...
    @cluster_ip.setter
    def cluster_ip(self, cluster_ip) -> None: ...
    @property
    def external_i_ps(self): ...
    @external_i_ps.setter
    def external_i_ps(self, external_i_ps) -> None: ...
    @property
    def external_name(self): ...
    @external_name.setter
    def external_name(self, external_name) -> None: ...
    @property
    def external_traffic_policy(self): ...
    @external_traffic_policy.setter
    def external_traffic_policy(self, external_traffic_policy) -> None: ...
    @property
    def health_check_node_port(self): ...
    @health_check_node_port.setter
    def health_check_node_port(self, health_check_node_port) -> None: ...
    @property
    def ip_family(self): ...
    @ip_family.setter
    def ip_family(self, ip_family) -> None: ...
    @property
    def load_balancer_ip(self): ...
    @load_balancer_ip.setter
    def load_balancer_ip(self, load_balancer_ip) -> None: ...
    @property
    def load_balancer_source_ranges(self): ...
    @load_balancer_source_ranges.setter
    def load_balancer_source_ranges(self, load_balancer_source_ranges) -> None: ...
    @property
    def ports(self): ...
    @ports.setter
    def ports(self, ports) -> None: ...
    @property
    def publish_not_ready_addresses(self): ...
    @publish_not_ready_addresses.setter
    def publish_not_ready_addresses(self, publish_not_ready_addresses) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector) -> None: ...
    @property
    def session_affinity(self): ...
    @session_affinity.setter
    def session_affinity(self, session_affinity) -> None: ...
    @property
    def session_affinity_config(self): ...
    @session_affinity_config.setter
    def session_affinity_config(self, session_affinity_config) -> None: ...
    @property
    def topology_keys(self): ...
    @topology_keys.setter
    def topology_keys(self, topology_keys) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

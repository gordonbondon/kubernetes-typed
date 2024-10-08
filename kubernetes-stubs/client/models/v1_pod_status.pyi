# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1PodStatus:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, conditions: Incomplete | None = None, container_statuses: Incomplete | None = None, ephemeral_container_statuses: Incomplete | None = None, host_ip: Incomplete | None = None, init_container_statuses: Incomplete | None = None, message: Incomplete | None = None, nominated_node_name: Incomplete | None = None, phase: Incomplete | None = None, pod_ip: Incomplete | None = None, pod_i_ps: Incomplete | None = None, qos_class: Incomplete | None = None, reason: Incomplete | None = None, start_time: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions) -> None: ...
    @property
    def container_statuses(self): ...
    @container_statuses.setter
    def container_statuses(self, container_statuses) -> None: ...
    @property
    def ephemeral_container_statuses(self): ...
    @ephemeral_container_statuses.setter
    def ephemeral_container_statuses(self, ephemeral_container_statuses) -> None: ...
    @property
    def host_ip(self): ...
    @host_ip.setter
    def host_ip(self, host_ip) -> None: ...
    @property
    def init_container_statuses(self): ...
    @init_container_statuses.setter
    def init_container_statuses(self, init_container_statuses) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    @property
    def nominated_node_name(self): ...
    @nominated_node_name.setter
    def nominated_node_name(self, nominated_node_name) -> None: ...
    @property
    def phase(self): ...
    @phase.setter
    def phase(self, phase) -> None: ...
    @property
    def pod_ip(self): ...
    @pod_ip.setter
    def pod_ip(self, pod_ip) -> None: ...
    @property
    def pod_i_ps(self): ...
    @pod_i_ps.setter
    def pod_i_ps(self, pod_i_ps) -> None: ...
    @property
    def qos_class(self): ...
    @qos_class.setter
    def qos_class(self, qos_class) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason) -> None: ...
    @property
    def start_time(self): ...
    @start_time.setter
    def start_time(self, start_time) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

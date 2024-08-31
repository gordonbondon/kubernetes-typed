# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1NodeSpec:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, config_source: Incomplete | None = None, external_id: Incomplete | None = None, pod_cidr: Incomplete | None = None, pod_cid_rs: Incomplete | None = None, provider_id: Incomplete | None = None, taints: Incomplete | None = None, unschedulable: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def config_source(self): ...
    @config_source.setter
    def config_source(self, config_source) -> None: ...
    @property
    def external_id(self): ...
    @external_id.setter
    def external_id(self, external_id) -> None: ...
    @property
    def pod_cidr(self): ...
    @pod_cidr.setter
    def pod_cidr(self, pod_cidr) -> None: ...
    @property
    def pod_cid_rs(self): ...
    @pod_cid_rs.setter
    def pod_cid_rs(self, pod_cid_rs) -> None: ...
    @property
    def provider_id(self): ...
    @provider_id.setter
    def provider_id(self, provider_id) -> None: ...
    @property
    def taints(self): ...
    @taints.setter
    def taints(self, taints) -> None: ...
    @property
    def unschedulable(self): ...
    @unschedulable.setter
    def unschedulable(self, unschedulable) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

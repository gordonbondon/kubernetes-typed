# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1NetworkPolicyPeer:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, ip_block: Incomplete | None = None, namespace_selector: Incomplete | None = None, pod_selector: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def ip_block(self): ...
    @ip_block.setter
    def ip_block(self, ip_block) -> None: ...
    @property
    def namespace_selector(self): ...
    @namespace_selector.setter
    def namespace_selector(self, namespace_selector) -> None: ...
    @property
    def pod_selector(self): ...
    @pod_selector.setter
    def pod_selector(self, pod_selector) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

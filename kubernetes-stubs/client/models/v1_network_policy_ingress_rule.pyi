# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1NetworkPolicyIngressRule:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, _from: Incomplete | None = None, ports: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def ports(self): ...
    @ports.setter
    def ports(self, ports) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

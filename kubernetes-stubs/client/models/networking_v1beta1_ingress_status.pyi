# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class NetworkingV1beta1IngressStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, load_balancer: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def load_balancer(self): ...
    @load_balancer.setter
    def load_balancer(self, load_balancer) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

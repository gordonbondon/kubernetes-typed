# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class ExtensionsV1beta1IngressBackend:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, service_name: Any | None = ..., service_port: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def service_name(self): ...
    @service_name.setter
    def service_name(self, service_name) -> None: ...
    @property
    def service_port(self): ...
    @service_port.setter
    def service_port(self, service_port) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1EventSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, component: Any | None = ..., host: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def component(self): ...
    @component.setter
    def component(self, component) -> None: ...
    @property
    def host(self): ...
    @host.setter
    def host(self, host) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

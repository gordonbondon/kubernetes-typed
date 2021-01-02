# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1EndpointSubset:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, addresses: Optional[Any] = ..., not_ready_addresses: Optional[Any] = ..., ports: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def addresses(self): ...
    @addresses.setter
    def addresses(self, addresses: Any) -> None: ...
    @property
    def not_ready_addresses(self): ...
    @not_ready_addresses.setter
    def not_ready_addresses(self, not_ready_addresses: Any) -> None: ...
    @property
    def ports(self): ...
    @ports.setter
    def ports(self, ports: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

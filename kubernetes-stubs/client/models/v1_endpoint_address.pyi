# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1EndpointAddress:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, hostname: Optional[Any] = ..., ip: Optional[Any] = ..., node_name: Optional[Any] = ..., target_ref: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def hostname(self): ...
    @hostname.setter
    def hostname(self, hostname: Any) -> None: ...
    @property
    def ip(self): ...
    @ip.setter
    def ip(self, ip: Any) -> None: ...
    @property
    def node_name(self): ...
    @node_name.setter
    def node_name(self, node_name: Any) -> None: ...
    @property
    def target_ref(self): ...
    @target_ref.setter
    def target_ref(self, target_ref: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

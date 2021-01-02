# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1NodeStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, addresses: Optional[Any] = ..., allocatable: Optional[Any] = ..., capacity: Optional[Any] = ..., conditions: Optional[Any] = ..., config: Optional[Any] = ..., daemon_endpoints: Optional[Any] = ..., images: Optional[Any] = ..., node_info: Optional[Any] = ..., phase: Optional[Any] = ..., volumes_attached: Optional[Any] = ..., volumes_in_use: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def addresses(self): ...
    @addresses.setter
    def addresses(self, addresses: Any) -> None: ...
    @property
    def allocatable(self): ...
    @allocatable.setter
    def allocatable(self, allocatable: Any) -> None: ...
    @property
    def capacity(self): ...
    @capacity.setter
    def capacity(self, capacity: Any) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions: Any) -> None: ...
    @property
    def config(self): ...
    @config.setter
    def config(self, config: Any) -> None: ...
    @property
    def daemon_endpoints(self): ...
    @daemon_endpoints.setter
    def daemon_endpoints(self, daemon_endpoints: Any) -> None: ...
    @property
    def images(self): ...
    @images.setter
    def images(self, images: Any) -> None: ...
    @property
    def node_info(self): ...
    @node_info.setter
    def node_info(self, node_info: Any) -> None: ...
    @property
    def phase(self): ...
    @phase.setter
    def phase(self, phase: Any) -> None: ...
    @property
    def volumes_attached(self): ...
    @volumes_attached.setter
    def volumes_attached(self, volumes_attached: Any) -> None: ...
    @property
    def volumes_in_use(self): ...
    @volumes_in_use.setter
    def volumes_in_use(self, volumes_in_use: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

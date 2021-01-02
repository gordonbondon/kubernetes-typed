from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class ApiextensionsV1beta1ServiceReference:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, name: Optional[Any] = ..., namespace: Optional[Any] = ..., path: Optional[Any] = ..., port: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def namespace(self): ...
    @namespace.setter
    def namespace(self, namespace: Any) -> None: ...
    @property
    def path(self): ...
    @path.setter
    def path(self, path: Any) -> None: ...
    @property
    def port(self): ...
    @port.setter
    def port(self, port: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1GlusterfsPersistentVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, endpoints: Optional[Any] = ..., endpoints_namespace: Optional[Any] = ..., path: Optional[Any] = ..., read_only: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def endpoints(self): ...
    @endpoints.setter
    def endpoints(self, endpoints: Any) -> None: ...
    @property
    def endpoints_namespace(self): ...
    @endpoints_namespace.setter
    def endpoints_namespace(self, endpoints_namespace: Any) -> None: ...
    @property
    def path(self): ...
    @path.setter
    def path(self, path: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1GlusterfsPersistentVolumeSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, endpoints: Any | None = ..., endpoints_namespace: Any | None = ..., path: Any | None = ..., read_only: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def endpoints(self): ...
    @endpoints.setter
    def endpoints(self, endpoints) -> None: ...
    @property
    def endpoints_namespace(self): ...
    @endpoints_namespace.setter
    def endpoints_namespace(self, endpoints_namespace) -> None: ...
    @property
    def path(self): ...
    @path.setter
    def path(self, path) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

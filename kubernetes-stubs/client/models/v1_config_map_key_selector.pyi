# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ConfigMapKeySelector:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, key: Any | None = ..., name: Any | None = ..., optional: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def optional(self): ...
    @optional.setter
    def optional(self, optional) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

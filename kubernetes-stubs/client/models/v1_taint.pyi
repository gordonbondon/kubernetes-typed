# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1Taint:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, effect: Any | None = ..., key: Any | None = ..., time_added: Any | None = ..., value: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def effect(self): ...
    @effect.setter
    def effect(self, effect) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key) -> None: ...
    @property
    def time_added(self): ...
    @time_added.setter
    def time_added(self, time_added) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

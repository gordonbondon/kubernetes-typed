# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V2beta2HPAScalingPolicy:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, period_seconds: Any | None = ..., type: Any | None = ..., value: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def period_seconds(self): ...
    @period_seconds.setter
    def period_seconds(self, period_seconds) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V2beta2MetricValueStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, average_utilization: Any | None = ..., average_value: Any | None = ..., value: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def average_utilization(self): ...
    @average_utilization.setter
    def average_utilization(self, average_utilization) -> None: ...
    @property
    def average_value(self): ...
    @average_value.setter
    def average_value(self, average_value) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

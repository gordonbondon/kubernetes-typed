# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2beta1ResourceMetricStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, current_average_utilization: Optional[Any] = ..., current_average_value: Optional[Any] = ..., name: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def current_average_utilization(self): ...
    @current_average_utilization.setter
    def current_average_utilization(self, current_average_utilization: Any) -> None: ...
    @property
    def current_average_value(self): ...
    @current_average_value.setter
    def current_average_value(self, current_average_value: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
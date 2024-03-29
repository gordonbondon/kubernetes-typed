# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V2beta1ExternalMetricSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, metric_name: Any | None = ..., metric_selector: Any | None = ..., target_average_value: Any | None = ..., target_value: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def metric_name(self): ...
    @metric_name.setter
    def metric_name(self, metric_name) -> None: ...
    @property
    def metric_selector(self): ...
    @metric_selector.setter
    def metric_selector(self, metric_selector) -> None: ...
    @property
    def target_average_value(self): ...
    @target_average_value.setter
    def target_average_value(self, target_average_value) -> None: ...
    @property
    def target_value(self): ...
    @target_value.setter
    def target_value(self, target_value) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

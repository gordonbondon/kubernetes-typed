from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2beta1ExternalMetricSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, metric_name: Optional[Any] = ..., metric_selector: Optional[Any] = ..., target_average_value: Optional[Any] = ..., target_value: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def metric_name(self): ...
    @metric_name.setter
    def metric_name(self, metric_name: Any) -> None: ...
    @property
    def metric_selector(self): ...
    @metric_selector.setter
    def metric_selector(self, metric_selector: Any) -> None: ...
    @property
    def target_average_value(self): ...
    @target_average_value.setter
    def target_average_value(self, target_average_value: Any) -> None: ...
    @property
    def target_value(self): ...
    @target_value.setter
    def target_value(self, target_value: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

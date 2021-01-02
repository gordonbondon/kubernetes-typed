from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2beta2ExternalMetricStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, current: Optional[Any] = ..., metric: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def current(self): ...
    @current.setter
    def current(self, current: Any) -> None: ...
    @property
    def metric(self): ...
    @metric.setter
    def metric(self, metric: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

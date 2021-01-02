from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2beta2ObjectMetricSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, described_object: Optional[Any] = ..., metric: Optional[Any] = ..., target: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def described_object(self): ...
    @described_object.setter
    def described_object(self, described_object: Any) -> None: ...
    @property
    def metric(self): ...
    @metric.setter
    def metric(self, metric: Any) -> None: ...
    @property
    def target(self): ...
    @target.setter
    def target(self, target: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

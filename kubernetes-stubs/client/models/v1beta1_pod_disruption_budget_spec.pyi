from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1PodDisruptionBudgetSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, max_unavailable: Optional[Any] = ..., min_available: Optional[Any] = ..., selector: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def max_unavailable(self): ...
    @max_unavailable.setter
    def max_unavailable(self, max_unavailable: Any) -> None: ...
    @property
    def min_available(self): ...
    @min_available.setter
    def min_available(self, min_available: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

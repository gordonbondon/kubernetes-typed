from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1alpha1RuntimeClassSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, overhead: Optional[Any] = ..., runtime_handler: Optional[Any] = ..., scheduling: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def overhead(self): ...
    @overhead.setter
    def overhead(self, overhead: Any) -> None: ...
    @property
    def runtime_handler(self): ...
    @runtime_handler.setter
    def runtime_handler(self, runtime_handler: Any) -> None: ...
    @property
    def scheduling(self): ...
    @scheduling.setter
    def scheduling(self, scheduling: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

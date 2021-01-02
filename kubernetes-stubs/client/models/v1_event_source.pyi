from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1EventSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, component: Optional[Any] = ..., host: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def component(self): ...
    @component.setter
    def component(self, component: Any) -> None: ...
    @property
    def host(self): ...
    @host.setter
    def host(self, host: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

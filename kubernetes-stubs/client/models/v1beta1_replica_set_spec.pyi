from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1ReplicaSetSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, min_ready_seconds: Optional[Any] = ..., replicas: Optional[Any] = ..., selector: Optional[Any] = ..., template: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def min_ready_seconds(self): ...
    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds: Any) -> None: ...
    @property
    def replicas(self): ...
    @replicas.setter
    def replicas(self, replicas: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    @property
    def template(self): ...
    @template.setter
    def template(self, template: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

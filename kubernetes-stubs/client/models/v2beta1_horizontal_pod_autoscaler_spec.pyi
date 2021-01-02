from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2beta1HorizontalPodAutoscalerSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, max_replicas: Optional[Any] = ..., metrics: Optional[Any] = ..., min_replicas: Optional[Any] = ..., scale_target_ref: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def max_replicas(self): ...
    @max_replicas.setter
    def max_replicas(self, max_replicas: Any) -> None: ...
    @property
    def metrics(self): ...
    @metrics.setter
    def metrics(self, metrics: Any) -> None: ...
    @property
    def min_replicas(self): ...
    @min_replicas.setter
    def min_replicas(self, min_replicas: Any) -> None: ...
    @property
    def scale_target_ref(self): ...
    @scale_target_ref.setter
    def scale_target_ref(self, scale_target_ref: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

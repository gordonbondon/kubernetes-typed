from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1PodDisruptionBudgetStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, current_healthy: Optional[Any] = ..., desired_healthy: Optional[Any] = ..., disrupted_pods: Optional[Any] = ..., disruptions_allowed: Optional[Any] = ..., expected_pods: Optional[Any] = ..., observed_generation: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def current_healthy(self): ...
    @current_healthy.setter
    def current_healthy(self, current_healthy: Any) -> None: ...
    @property
    def desired_healthy(self): ...
    @desired_healthy.setter
    def desired_healthy(self, desired_healthy: Any) -> None: ...
    @property
    def disrupted_pods(self): ...
    @disrupted_pods.setter
    def disrupted_pods(self, disrupted_pods: Any) -> None: ...
    @property
    def disruptions_allowed(self): ...
    @disruptions_allowed.setter
    def disruptions_allowed(self, disruptions_allowed: Any) -> None: ...
    @property
    def expected_pods(self): ...
    @expected_pods.setter
    def expected_pods(self, expected_pods: Any) -> None: ...
    @property
    def observed_generation(self): ...
    @observed_generation.setter
    def observed_generation(self, observed_generation: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

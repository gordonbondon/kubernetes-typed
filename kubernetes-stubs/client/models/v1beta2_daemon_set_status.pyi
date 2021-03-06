# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta2DaemonSetStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, collision_count: Optional[Any] = ..., conditions: Optional[Any] = ..., current_number_scheduled: Optional[Any] = ..., desired_number_scheduled: Optional[Any] = ..., number_available: Optional[Any] = ..., number_misscheduled: Optional[Any] = ..., number_ready: Optional[Any] = ..., number_unavailable: Optional[Any] = ..., observed_generation: Optional[Any] = ..., updated_number_scheduled: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def collision_count(self): ...
    @collision_count.setter
    def collision_count(self, collision_count: Any) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions: Any) -> None: ...
    @property
    def current_number_scheduled(self): ...
    @current_number_scheduled.setter
    def current_number_scheduled(self, current_number_scheduled: Any) -> None: ...
    @property
    def desired_number_scheduled(self): ...
    @desired_number_scheduled.setter
    def desired_number_scheduled(self, desired_number_scheduled: Any) -> None: ...
    @property
    def number_available(self): ...
    @number_available.setter
    def number_available(self, number_available: Any) -> None: ...
    @property
    def number_misscheduled(self): ...
    @number_misscheduled.setter
    def number_misscheduled(self, number_misscheduled: Any) -> None: ...
    @property
    def number_ready(self): ...
    @number_ready.setter
    def number_ready(self, number_ready: Any) -> None: ...
    @property
    def number_unavailable(self): ...
    @number_unavailable.setter
    def number_unavailable(self, number_unavailable: Any) -> None: ...
    @property
    def observed_generation(self): ...
    @observed_generation.setter
    def observed_generation(self, observed_generation: Any) -> None: ...
    @property
    def updated_number_scheduled(self): ...
    @updated_number_scheduled.setter
    def updated_number_scheduled(self, updated_number_scheduled: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

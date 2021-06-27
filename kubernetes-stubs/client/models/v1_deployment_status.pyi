# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1DeploymentStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, available_replicas: Any | None = ..., collision_count: Any | None = ..., conditions: Any | None = ..., observed_generation: Any | None = ..., ready_replicas: Any | None = ..., replicas: Any | None = ..., unavailable_replicas: Any | None = ..., updated_replicas: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def available_replicas(self): ...
    @available_replicas.setter
    def available_replicas(self, available_replicas) -> None: ...
    @property
    def collision_count(self): ...
    @collision_count.setter
    def collision_count(self, collision_count) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions) -> None: ...
    @property
    def observed_generation(self): ...
    @observed_generation.setter
    def observed_generation(self, observed_generation) -> None: ...
    @property
    def ready_replicas(self): ...
    @ready_replicas.setter
    def ready_replicas(self, ready_replicas) -> None: ...
    @property
    def replicas(self): ...
    @replicas.setter
    def replicas(self, replicas) -> None: ...
    @property
    def unavailable_replicas(self): ...
    @unavailable_replicas.setter
    def unavailable_replicas(self, unavailable_replicas) -> None: ...
    @property
    def updated_replicas(self): ...
    @updated_replicas.setter
    def updated_replicas(self, updated_replicas) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

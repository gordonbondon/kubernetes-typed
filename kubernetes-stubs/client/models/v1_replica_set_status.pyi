# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ReplicaSetStatus:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, available_replicas: Incomplete | None = None, conditions: Incomplete | None = None, fully_labeled_replicas: Incomplete | None = None, observed_generation: Incomplete | None = None, ready_replicas: Incomplete | None = None, replicas: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def available_replicas(self): ...
    @available_replicas.setter
    def available_replicas(self, available_replicas) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions) -> None: ...
    @property
    def fully_labeled_replicas(self): ...
    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, fully_labeled_replicas) -> None: ...
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
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

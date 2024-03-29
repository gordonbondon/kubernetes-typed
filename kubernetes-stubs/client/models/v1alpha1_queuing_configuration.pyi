# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1alpha1QueuingConfiguration:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, hand_size: Any | None = ..., queue_length_limit: Any | None = ..., queues: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def hand_size(self): ...
    @hand_size.setter
    def hand_size(self, hand_size) -> None: ...
    @property
    def queue_length_limit(self): ...
    @queue_length_limit.setter
    def queue_length_limit(self, queue_length_limit) -> None: ...
    @property
    def queues(self): ...
    @queues.setter
    def queues(self, queues) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1alpha1QueuingConfiguration:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, hand_size: Incomplete | None = None, queue_length_limit: Incomplete | None = None, queues: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
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

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1PodReadinessGate:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, condition_type: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def condition_type(self): ...
    @condition_type.setter
    def condition_type(self, condition_type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

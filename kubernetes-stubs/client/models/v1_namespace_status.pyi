# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1NamespaceStatus:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, conditions: Incomplete | None = None, phase: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions) -> None: ...
    @property
    def phase(self): ...
    @phase.setter
    def phase(self, phase) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

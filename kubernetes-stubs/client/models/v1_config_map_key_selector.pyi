# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ConfigMapKeySelector:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, key: Incomplete | None = None, name: Incomplete | None = None, optional: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def optional(self): ...
    @optional.setter
    def optional(self, optional) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

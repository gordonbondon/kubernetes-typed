# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1VolumeDevice:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, device_path: Incomplete | None = None, name: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def device_path(self): ...
    @device_path.setter
    def device_path(self, device_path) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1NFSVolumeSource:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, path: Incomplete | None = None, read_only: Incomplete | None = None, server: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def path(self): ...
    @path.setter
    def path(self, path) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def server(self): ...
    @server.setter
    def server(self, server) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

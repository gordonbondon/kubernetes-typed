# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1QuobyteVolumeSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, group: Any | None = ..., read_only: Any | None = ..., registry: Any | None = ..., tenant: Any | None = ..., user: Any | None = ..., volume: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def registry(self): ...
    @registry.setter
    def registry(self, registry) -> None: ...
    @property
    def tenant(self): ...
    @tenant.setter
    def tenant(self, tenant) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user) -> None: ...
    @property
    def volume(self): ...
    @volume.setter
    def volume(self, volume) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

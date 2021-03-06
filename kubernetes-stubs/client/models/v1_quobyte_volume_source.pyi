# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1QuobyteVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, group: Optional[Any] = ..., read_only: Optional[Any] = ..., registry: Optional[Any] = ..., tenant: Optional[Any] = ..., user: Optional[Any] = ..., volume: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    @property
    def registry(self): ...
    @registry.setter
    def registry(self, registry: Any) -> None: ...
    @property
    def tenant(self): ...
    @tenant.setter
    def tenant(self, tenant: Any) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user: Any) -> None: ...
    @property
    def volume(self): ...
    @volume.setter
    def volume(self, volume: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

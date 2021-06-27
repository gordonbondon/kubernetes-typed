# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1CinderPersistentVolumeSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, fs_type: Any | None = ..., read_only: Any | None = ..., secret_ref: Any | None = ..., volume_id: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def secret_ref(self): ...
    @secret_ref.setter
    def secret_ref(self, secret_ref) -> None: ...
    @property
    def volume_id(self): ...
    @volume_id.setter
    def volume_id(self, volume_id) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

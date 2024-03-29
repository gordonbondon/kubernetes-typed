# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1VolumeMount:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, mount_path: Any | None = ..., mount_propagation: Any | None = ..., name: Any | None = ..., read_only: Any | None = ..., sub_path: Any | None = ..., sub_path_expr: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def mount_path(self): ...
    @mount_path.setter
    def mount_path(self, mount_path) -> None: ...
    @property
    def mount_propagation(self): ...
    @mount_propagation.setter
    def mount_propagation(self, mount_propagation) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def sub_path(self): ...
    @sub_path.setter
    def sub_path(self, sub_path) -> None: ...
    @property
    def sub_path_expr(self): ...
    @sub_path_expr.setter
    def sub_path_expr(self, sub_path_expr) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1CSIDriverSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, attach_required: Any | None = ..., pod_info_on_mount: Any | None = ..., volume_lifecycle_modes: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def attach_required(self): ...
    @attach_required.setter
    def attach_required(self, attach_required) -> None: ...
    @property
    def pod_info_on_mount(self): ...
    @pod_info_on_mount.setter
    def pod_info_on_mount(self, pod_info_on_mount) -> None: ...
    @property
    def volume_lifecycle_modes(self): ...
    @volume_lifecycle_modes.setter
    def volume_lifecycle_modes(self, volume_lifecycle_modes) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

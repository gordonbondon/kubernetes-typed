# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1alpha1VolumeAttachmentSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, inline_volume_spec: Any | None = ..., persistent_volume_name: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def inline_volume_spec(self): ...
    @inline_volume_spec.setter
    def inline_volume_spec(self, inline_volume_spec) -> None: ...
    @property
    def persistent_volume_name(self): ...
    @persistent_volume_name.setter
    def persistent_volume_name(self, persistent_volume_name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1VolumeAttachmentSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, inline_volume_spec: Optional[Any] = ..., persistent_volume_name: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def inline_volume_spec(self): ...
    @inline_volume_spec.setter
    def inline_volume_spec(self, inline_volume_spec: Any) -> None: ...
    @property
    def persistent_volume_name(self): ...
    @persistent_volume_name.setter
    def persistent_volume_name(self, persistent_volume_name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

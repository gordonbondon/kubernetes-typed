from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1AzureDiskVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, caching_mode: Optional[Any] = ..., disk_name: Optional[Any] = ..., disk_uri: Optional[Any] = ..., fs_type: Optional[Any] = ..., kind: Optional[Any] = ..., read_only: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def caching_mode(self): ...
    @caching_mode.setter
    def caching_mode(self, caching_mode: Any) -> None: ...
    @property
    def disk_name(self): ...
    @disk_name.setter
    def disk_name(self, disk_name: Any) -> None: ...
    @property
    def disk_uri(self): ...
    @disk_uri.setter
    def disk_uri(self, disk_uri: Any) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

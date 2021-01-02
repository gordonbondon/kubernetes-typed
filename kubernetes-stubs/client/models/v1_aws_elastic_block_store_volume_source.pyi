from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1AWSElasticBlockStoreVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, fs_type: Optional[Any] = ..., partition: Optional[Any] = ..., read_only: Optional[Any] = ..., volume_id: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type: Any) -> None: ...
    @property
    def partition(self): ...
    @partition.setter
    def partition(self, partition: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    @property
    def volume_id(self): ...
    @volume_id.setter
    def volume_id(self, volume_id: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1ScaleIOPersistentVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, fs_type: Optional[Any] = ..., gateway: Optional[Any] = ..., protection_domain: Optional[Any] = ..., read_only: Optional[Any] = ..., secret_ref: Optional[Any] = ..., ssl_enabled: Optional[Any] = ..., storage_mode: Optional[Any] = ..., storage_pool: Optional[Any] = ..., system: Optional[Any] = ..., volume_name: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type: Any) -> None: ...
    @property
    def gateway(self): ...
    @gateway.setter
    def gateway(self, gateway: Any) -> None: ...
    @property
    def protection_domain(self): ...
    @protection_domain.setter
    def protection_domain(self, protection_domain: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    @property
    def secret_ref(self): ...
    @secret_ref.setter
    def secret_ref(self, secret_ref: Any) -> None: ...
    @property
    def ssl_enabled(self): ...
    @ssl_enabled.setter
    def ssl_enabled(self, ssl_enabled: Any) -> None: ...
    @property
    def storage_mode(self): ...
    @storage_mode.setter
    def storage_mode(self, storage_mode: Any) -> None: ...
    @property
    def storage_pool(self): ...
    @storage_pool.setter
    def storage_pool(self, storage_pool: Any) -> None: ...
    @property
    def system(self): ...
    @system.setter
    def system(self, system: Any) -> None: ...
    @property
    def volume_name(self): ...
    @volume_name.setter
    def volume_name(self, volume_name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

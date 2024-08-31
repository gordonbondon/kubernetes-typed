# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ScaleIOPersistentVolumeSource:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, fs_type: Incomplete | None = None, gateway: Incomplete | None = None, protection_domain: Incomplete | None = None, read_only: Incomplete | None = None, secret_ref: Incomplete | None = None, ssl_enabled: Incomplete | None = None, storage_mode: Incomplete | None = None, storage_pool: Incomplete | None = None, system: Incomplete | None = None, volume_name: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type) -> None: ...
    @property
    def gateway(self): ...
    @gateway.setter
    def gateway(self, gateway) -> None: ...
    @property
    def protection_domain(self): ...
    @protection_domain.setter
    def protection_domain(self, protection_domain) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def secret_ref(self): ...
    @secret_ref.setter
    def secret_ref(self, secret_ref) -> None: ...
    @property
    def ssl_enabled(self): ...
    @ssl_enabled.setter
    def ssl_enabled(self, ssl_enabled) -> None: ...
    @property
    def storage_mode(self): ...
    @storage_mode.setter
    def storage_mode(self, storage_mode) -> None: ...
    @property
    def storage_pool(self): ...
    @storage_pool.setter
    def storage_pool(self, storage_pool) -> None: ...
    @property
    def system(self): ...
    @system.setter
    def system(self, system) -> None: ...
    @property
    def volume_name(self): ...
    @volume_name.setter
    def volume_name(self, volume_name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

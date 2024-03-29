# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1StorageClass:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, allow_volume_expansion: Any | None = ..., allowed_topologies: Any | None = ..., api_version: Any | None = ..., kind: Any | None = ..., metadata: Any | None = ..., mount_options: Any | None = ..., parameters: Any | None = ..., provisioner: Any | None = ..., reclaim_policy: Any | None = ..., volume_binding_mode: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def allow_volume_expansion(self): ...
    @allow_volume_expansion.setter
    def allow_volume_expansion(self, allow_volume_expansion) -> None: ...
    @property
    def allowed_topologies(self): ...
    @allowed_topologies.setter
    def allowed_topologies(self, allowed_topologies) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata) -> None: ...
    @property
    def mount_options(self): ...
    @mount_options.setter
    def mount_options(self, mount_options) -> None: ...
    @property
    def parameters(self): ...
    @parameters.setter
    def parameters(self, parameters) -> None: ...
    @property
    def provisioner(self): ...
    @provisioner.setter
    def provisioner(self, provisioner) -> None: ...
    @property
    def reclaim_policy(self): ...
    @reclaim_policy.setter
    def reclaim_policy(self, reclaim_policy) -> None: ...
    @property
    def volume_binding_mode(self): ...
    @volume_binding_mode.setter
    def volume_binding_mode(self, volume_binding_mode) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

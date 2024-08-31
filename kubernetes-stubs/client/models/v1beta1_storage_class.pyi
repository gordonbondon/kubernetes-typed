# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1beta1StorageClass:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, allow_volume_expansion: Incomplete | None = None, allowed_topologies: Incomplete | None = None, api_version: Incomplete | None = None, kind: Incomplete | None = None, metadata: Incomplete | None = None, mount_options: Incomplete | None = None, parameters: Incomplete | None = None, provisioner: Incomplete | None = None, reclaim_policy: Incomplete | None = None, volume_binding_mode: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
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

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1PersistentVolumeClaimSpec:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, access_modes: Incomplete | None = None, data_source: Incomplete | None = None, resources: Incomplete | None = None, selector: Incomplete | None = None, storage_class_name: Incomplete | None = None, volume_mode: Incomplete | None = None, volume_name: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def access_modes(self): ...
    @access_modes.setter
    def access_modes(self, access_modes) -> None: ...
    @property
    def data_source(self): ...
    @data_source.setter
    def data_source(self, data_source) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector) -> None: ...
    @property
    def storage_class_name(self): ...
    @storage_class_name.setter
    def storage_class_name(self, storage_class_name) -> None: ...
    @property
    def volume_mode(self): ...
    @volume_mode.setter
    def volume_mode(self, volume_mode) -> None: ...
    @property
    def volume_name(self): ...
    @volume_name.setter
    def volume_name(self, volume_name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

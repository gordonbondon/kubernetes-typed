# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1PhotonPersistentDiskVolumeSource:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, fs_type: Incomplete | None = None, pd_id: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type) -> None: ...
    @property
    def pd_id(self): ...
    @pd_id.setter
    def pd_id(self, pd_id) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1FCVolumeSource:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, fs_type: Incomplete | None = None, lun: Incomplete | None = None, read_only: Incomplete | None = None, target_ww_ns: Incomplete | None = None, wwids: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type) -> None: ...
    @property
    def lun(self): ...
    @lun.setter
    def lun(self, lun) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def target_ww_ns(self): ...
    @target_ww_ns.setter
    def target_ww_ns(self, target_ww_ns) -> None: ...
    @property
    def wwids(self): ...
    @wwids.setter
    def wwids(self, wwids) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

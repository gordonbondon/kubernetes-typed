# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1alpha1NonResourcePolicyRule:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, non_resource_ur_ls: Incomplete | None = None, verbs: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def non_resource_ur_ls(self): ...
    @non_resource_ur_ls.setter
    def non_resource_ur_ls(self, non_resource_ur_ls) -> None: ...
    @property
    def verbs(self): ...
    @verbs.setter
    def verbs(self, verbs) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

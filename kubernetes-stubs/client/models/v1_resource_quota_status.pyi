# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ResourceQuotaStatus:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, hard: Incomplete | None = None, used: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def hard(self): ...
    @hard.setter
    def hard(self, hard) -> None: ...
    @property
    def used(self): ...
    @used.setter
    def used(self, used) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

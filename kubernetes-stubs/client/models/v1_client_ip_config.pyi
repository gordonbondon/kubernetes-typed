# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ClientIPConfig:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, timeout_seconds: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def timeout_seconds(self): ...
    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1LimitRangeItem:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, default: Incomplete | None = None, default_request: Incomplete | None = None, max: Incomplete | None = None, max_limit_request_ratio: Incomplete | None = None, min: Incomplete | None = None, type: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def default(self): ...
    @default.setter
    def default(self, default) -> None: ...
    @property
    def default_request(self): ...
    @default_request.setter
    def default_request(self, default_request) -> None: ...
    @property
    def max(self): ...
    @max.setter
    def max(self, max) -> None: ...
    @property
    def max_limit_request_ratio(self): ...
    @max_limit_request_ratio.setter
    def max_limit_request_ratio(self, max_limit_request_ratio) -> None: ...
    @property
    def min(self): ...
    @min.setter
    def min(self, min) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

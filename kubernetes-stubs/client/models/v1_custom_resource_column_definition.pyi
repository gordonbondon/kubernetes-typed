# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1CustomResourceColumnDefinition:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, description: Incomplete | None = None, format: Incomplete | None = None, json_path: Incomplete | None = None, name: Incomplete | None = None, priority: Incomplete | None = None, type: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def format(self): ...
    @format.setter
    def format(self, format) -> None: ...
    @property
    def json_path(self): ...
    @json_path.setter
    def json_path(self, json_path) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def priority(self): ...
    @priority.setter
    def priority(self, priority) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

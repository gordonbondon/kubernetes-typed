# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1CustomResourceColumnDefinition:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, description: Optional[Any] = ..., format: Optional[Any] = ..., json_path: Optional[Any] = ..., name: Optional[Any] = ..., priority: Optional[Any] = ..., type: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description: Any) -> None: ...
    @property
    def format(self): ...
    @format.setter
    def format(self, format: Any) -> None: ...
    @property
    def json_path(self): ...
    @json_path.setter
    def json_path(self, json_path: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def priority(self): ...
    @priority.setter
    def priority(self, priority: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
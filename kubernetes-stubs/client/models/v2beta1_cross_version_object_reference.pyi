# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2beta1CrossVersionObjectReference:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, api_version: Optional[Any] = ..., kind: Optional[Any] = ..., name: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

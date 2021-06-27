# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ObjectReference:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, api_version: Any | None = ..., field_path: Any | None = ..., kind: Any | None = ..., name: Any | None = ..., namespace: Any | None = ..., resource_version: Any | None = ..., uid: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def field_path(self): ...
    @field_path.setter
    def field_path(self, field_path) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def namespace(self): ...
    @namespace.setter
    def namespace(self, namespace) -> None: ...
    @property
    def resource_version(self): ...
    @resource_version.setter
    def resource_version(self, resource_version) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1ResourceAttributes:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, group: Optional[Any] = ..., name: Optional[Any] = ..., namespace: Optional[Any] = ..., resource: Optional[Any] = ..., subresource: Optional[Any] = ..., verb: Optional[Any] = ..., version: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def namespace(self): ...
    @namespace.setter
    def namespace(self, namespace: Any) -> None: ...
    @property
    def resource(self): ...
    @resource.setter
    def resource(self, resource: Any) -> None: ...
    @property
    def subresource(self): ...
    @subresource.setter
    def subresource(self, subresource: Any) -> None: ...
    @property
    def verb(self): ...
    @verb.setter
    def verb(self, verb: Any) -> None: ...
    @property
    def version(self): ...
    @version.setter
    def version(self, version: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

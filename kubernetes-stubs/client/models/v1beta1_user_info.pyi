# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1UserInfo:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, extra: Optional[Any] = ..., groups: Optional[Any] = ..., uid: Optional[Any] = ..., username: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def extra(self): ...
    @extra.setter
    def extra(self, extra: Any) -> None: ...
    @property
    def groups(self): ...
    @groups.setter
    def groups(self, groups: Any) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid: Any) -> None: ...
    @property
    def username(self): ...
    @username.setter
    def username(self, username: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

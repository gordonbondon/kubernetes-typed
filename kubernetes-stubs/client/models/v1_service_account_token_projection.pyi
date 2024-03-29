# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ServiceAccountTokenProjection:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, audience: Any | None = ..., expiration_seconds: Any | None = ..., path: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def audience(self): ...
    @audience.setter
    def audience(self, audience) -> None: ...
    @property
    def expiration_seconds(self): ...
    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds) -> None: ...
    @property
    def path(self): ...
    @path.setter
    def path(self, path) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

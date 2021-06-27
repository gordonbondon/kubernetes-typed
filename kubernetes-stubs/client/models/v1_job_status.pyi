# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1JobStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, active: Any | None = ..., completion_time: Any | None = ..., conditions: Any | None = ..., failed: Any | None = ..., start_time: Any | None = ..., succeeded: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def active(self): ...
    @active.setter
    def active(self, active) -> None: ...
    @property
    def completion_time(self): ...
    @completion_time.setter
    def completion_time(self, completion_time) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions) -> None: ...
    @property
    def failed(self): ...
    @failed.setter
    def failed(self, failed) -> None: ...
    @property
    def start_time(self): ...
    @start_time.setter
    def start_time(self, start_time) -> None: ...
    @property
    def succeeded(self): ...
    @succeeded.setter
    def succeeded(self, succeeded) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta2ScaleStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, replicas: Any | None = ..., selector: Any | None = ..., target_selector: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def replicas(self): ...
    @replicas.setter
    def replicas(self, replicas) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector) -> None: ...
    @property
    def target_selector(self): ...
    @target_selector.setter
    def target_selector(self, target_selector) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

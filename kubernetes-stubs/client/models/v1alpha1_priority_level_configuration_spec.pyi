# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1alpha1PriorityLevelConfigurationSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, limited: Any | None = ..., type: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def limited(self): ...
    @limited.setter
    def limited(self, limited) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1CustomResourceDefinitionStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, accepted_names: Any | None = ..., conditions: Any | None = ..., stored_versions: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def accepted_names(self): ...
    @accepted_names.setter
    def accepted_names(self, accepted_names) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions) -> None: ...
    @property
    def stored_versions(self): ...
    @stored_versions.setter
    def stored_versions(self, stored_versions) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

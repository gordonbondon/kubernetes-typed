# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1SelfSubjectAccessReviewSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, non_resource_attributes: Any | None = ..., resource_attributes: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def non_resource_attributes(self): ...
    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes) -> None: ...
    @property
    def resource_attributes(self): ...
    @resource_attributes.setter
    def resource_attributes(self, resource_attributes) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

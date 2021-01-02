from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1SelfSubjectAccessReviewSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, non_resource_attributes: Optional[Any] = ..., resource_attributes: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def non_resource_attributes(self): ...
    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes: Any) -> None: ...
    @property
    def resource_attributes(self): ...
    @resource_attributes.setter
    def resource_attributes(self, resource_attributes: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1AggregationRule:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, cluster_role_selectors: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def cluster_role_selectors(self): ...
    @cluster_role_selectors.setter
    def cluster_role_selectors(self, cluster_role_selectors: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

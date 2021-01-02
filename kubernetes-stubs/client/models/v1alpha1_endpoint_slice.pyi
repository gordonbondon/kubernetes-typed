from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1alpha1EndpointSlice:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, address_type: Optional[Any] = ..., api_version: Optional[Any] = ..., endpoints: Optional[Any] = ..., kind: Optional[Any] = ..., metadata: Optional[Any] = ..., ports: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def address_type(self): ...
    @address_type.setter
    def address_type(self, address_type: Any) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version: Any) -> None: ...
    @property
    def endpoints(self): ...
    @endpoints.setter
    def endpoints(self, endpoints: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata: Any) -> None: ...
    @property
    def ports(self): ...
    @ports.setter
    def ports(self, ports: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

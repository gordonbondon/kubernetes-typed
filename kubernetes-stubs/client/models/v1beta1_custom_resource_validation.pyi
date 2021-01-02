from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1CustomResourceValidation:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, open_apiv3_schema: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def open_apiv3_schema(self): ...
    @open_apiv3_schema.setter
    def open_apiv3_schema(self, open_apiv3_schema: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

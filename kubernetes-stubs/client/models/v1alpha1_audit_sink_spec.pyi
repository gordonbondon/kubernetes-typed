from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1alpha1AuditSinkSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, policy: Optional[Any] = ..., webhook: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def policy(self): ...
    @policy.setter
    def policy(self, policy: Any) -> None: ...
    @property
    def webhook(self): ...
    @webhook.setter
    def webhook(self, webhook: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

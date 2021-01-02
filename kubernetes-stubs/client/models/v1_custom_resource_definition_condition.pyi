from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1CustomResourceDefinitionCondition:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, last_transition_time: Optional[Any] = ..., message: Optional[Any] = ..., reason: Optional[Any] = ..., status: Optional[Any] = ..., type: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def last_transition_time(self): ...
    @last_transition_time.setter
    def last_transition_time(self, last_transition_time: Any) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message: Any) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason: Any) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

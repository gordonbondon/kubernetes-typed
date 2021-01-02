# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1PodAffinity:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, preferred_during_scheduling_ignored_during_execution: Optional[Any] = ..., required_during_scheduling_ignored_during_execution: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def preferred_during_scheduling_ignored_during_execution(self): ...
    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution: Any) -> None: ...
    @property
    def required_during_scheduling_ignored_during_execution(self): ...
    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

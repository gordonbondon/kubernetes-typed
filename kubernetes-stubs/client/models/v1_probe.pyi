from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1Probe:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, _exec: Optional[Any] = ..., failure_threshold: Optional[Any] = ..., http_get: Optional[Any] = ..., initial_delay_seconds: Optional[Any] = ..., period_seconds: Optional[Any] = ..., success_threshold: Optional[Any] = ..., tcp_socket: Optional[Any] = ..., timeout_seconds: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def failure_threshold(self): ...
    @failure_threshold.setter
    def failure_threshold(self, failure_threshold: Any) -> None: ...
    @property
    def http_get(self): ...
    @http_get.setter
    def http_get(self, http_get: Any) -> None: ...
    @property
    def initial_delay_seconds(self): ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds: Any) -> None: ...
    @property
    def period_seconds(self): ...
    @period_seconds.setter
    def period_seconds(self, period_seconds: Any) -> None: ...
    @property
    def success_threshold(self): ...
    @success_threshold.setter
    def success_threshold(self, success_threshold: Any) -> None: ...
    @property
    def tcp_socket(self): ...
    @tcp_socket.setter
    def tcp_socket(self, tcp_socket: Any) -> None: ...
    @property
    def timeout_seconds(self): ...
    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1alpha1PodPresetSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, env: Optional[Any] = ..., env_from: Optional[Any] = ..., selector: Optional[Any] = ..., volume_mounts: Optional[Any] = ..., volumes: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def env(self): ...
    @env.setter
    def env(self, env: Any) -> None: ...
    @property
    def env_from(self): ...
    @env_from.setter
    def env_from(self, env_from: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    @property
    def volume_mounts(self): ...
    @volume_mounts.setter
    def volume_mounts(self, volume_mounts: Any) -> None: ...
    @property
    def volumes(self): ...
    @volumes.setter
    def volumes(self, volumes: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

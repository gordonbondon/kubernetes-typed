# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1EphemeralContainer:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, args: Optional[Any] = ..., command: Optional[Any] = ..., env: Optional[Any] = ..., env_from: Optional[Any] = ..., image: Optional[Any] = ..., image_pull_policy: Optional[Any] = ..., lifecycle: Optional[Any] = ..., liveness_probe: Optional[Any] = ..., name: Optional[Any] = ..., ports: Optional[Any] = ..., readiness_probe: Optional[Any] = ..., resources: Optional[Any] = ..., security_context: Optional[Any] = ..., startup_probe: Optional[Any] = ..., stdin: Optional[Any] = ..., stdin_once: Optional[Any] = ..., target_container_name: Optional[Any] = ..., termination_message_path: Optional[Any] = ..., termination_message_policy: Optional[Any] = ..., tty: Optional[Any] = ..., volume_devices: Optional[Any] = ..., volume_mounts: Optional[Any] = ..., working_dir: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def args(self): ...
    @args.setter
    def args(self, args: Any) -> None: ...
    @property
    def command(self): ...
    @command.setter
    def command(self, command: Any) -> None: ...
    @property
    def env(self): ...
    @env.setter
    def env(self, env: Any) -> None: ...
    @property
    def env_from(self): ...
    @env_from.setter
    def env_from(self, env_from: Any) -> None: ...
    @property
    def image(self): ...
    @image.setter
    def image(self, image: Any) -> None: ...
    @property
    def image_pull_policy(self): ...
    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy: Any) -> None: ...
    @property
    def lifecycle(self): ...
    @lifecycle.setter
    def lifecycle(self, lifecycle: Any) -> None: ...
    @property
    def liveness_probe(self): ...
    @liveness_probe.setter
    def liveness_probe(self, liveness_probe: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def ports(self): ...
    @ports.setter
    def ports(self, ports: Any) -> None: ...
    @property
    def readiness_probe(self): ...
    @readiness_probe.setter
    def readiness_probe(self, readiness_probe: Any) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources: Any) -> None: ...
    @property
    def security_context(self): ...
    @security_context.setter
    def security_context(self, security_context: Any) -> None: ...
    @property
    def startup_probe(self): ...
    @startup_probe.setter
    def startup_probe(self, startup_probe: Any) -> None: ...
    @property
    def stdin(self): ...
    @stdin.setter
    def stdin(self, stdin: Any) -> None: ...
    @property
    def stdin_once(self): ...
    @stdin_once.setter
    def stdin_once(self, stdin_once: Any) -> None: ...
    @property
    def target_container_name(self): ...
    @target_container_name.setter
    def target_container_name(self, target_container_name: Any) -> None: ...
    @property
    def termination_message_path(self): ...
    @termination_message_path.setter
    def termination_message_path(self, termination_message_path: Any) -> None: ...
    @property
    def termination_message_policy(self): ...
    @termination_message_policy.setter
    def termination_message_policy(self, termination_message_policy: Any) -> None: ...
    @property
    def tty(self): ...
    @tty.setter
    def tty(self, tty: Any) -> None: ...
    @property
    def volume_devices(self): ...
    @volume_devices.setter
    def volume_devices(self, volume_devices: Any) -> None: ...
    @property
    def volume_mounts(self): ...
    @volume_mounts.setter
    def volume_mounts(self, volume_mounts: Any) -> None: ...
    @property
    def working_dir(self): ...
    @working_dir.setter
    def working_dir(self, working_dir: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

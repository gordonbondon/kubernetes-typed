# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1SecurityContext:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, allow_privilege_escalation: Incomplete | None = None, capabilities: Incomplete | None = None, privileged: Incomplete | None = None, proc_mount: Incomplete | None = None, read_only_root_filesystem: Incomplete | None = None, run_as_group: Incomplete | None = None, run_as_non_root: Incomplete | None = None, run_as_user: Incomplete | None = None, se_linux_options: Incomplete | None = None, windows_options: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def allow_privilege_escalation(self): ...
    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation) -> None: ...
    @property
    def capabilities(self): ...
    @capabilities.setter
    def capabilities(self, capabilities) -> None: ...
    @property
    def privileged(self): ...
    @privileged.setter
    def privileged(self, privileged) -> None: ...
    @property
    def proc_mount(self): ...
    @proc_mount.setter
    def proc_mount(self, proc_mount) -> None: ...
    @property
    def read_only_root_filesystem(self): ...
    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem) -> None: ...
    @property
    def run_as_group(self): ...
    @run_as_group.setter
    def run_as_group(self, run_as_group) -> None: ...
    @property
    def run_as_non_root(self): ...
    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root) -> None: ...
    @property
    def run_as_user(self): ...
    @run_as_user.setter
    def run_as_user(self, run_as_user) -> None: ...
    @property
    def se_linux_options(self): ...
    @se_linux_options.setter
    def se_linux_options(self, se_linux_options) -> None: ...
    @property
    def windows_options(self): ...
    @windows_options.setter
    def windows_options(self, windows_options) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

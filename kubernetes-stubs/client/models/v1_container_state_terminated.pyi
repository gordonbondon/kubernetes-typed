# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ContainerStateTerminated:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, container_id: Incomplete | None = None, exit_code: Incomplete | None = None, finished_at: Incomplete | None = None, message: Incomplete | None = None, reason: Incomplete | None = None, signal: Incomplete | None = None, started_at: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def container_id(self): ...
    @container_id.setter
    def container_id(self, container_id) -> None: ...
    @property
    def exit_code(self): ...
    @exit_code.setter
    def exit_code(self, exit_code) -> None: ...
    @property
    def finished_at(self): ...
    @finished_at.setter
    def finished_at(self, finished_at) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason) -> None: ...
    @property
    def signal(self): ...
    @signal.setter
    def signal(self, signal) -> None: ...
    @property
    def started_at(self): ...
    @started_at.setter
    def started_at(self, started_at) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

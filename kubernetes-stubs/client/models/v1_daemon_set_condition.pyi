# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1DaemonSetCondition:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, last_transition_time: Incomplete | None = None, message: Incomplete | None = None, reason: Incomplete | None = None, status: Incomplete | None = None, type: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def last_transition_time(self): ...
    @last_transition_time.setter
    def last_transition_time(self, last_transition_time) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

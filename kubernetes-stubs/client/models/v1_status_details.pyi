# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1StatusDetails:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, causes: Incomplete | None = None, group: Incomplete | None = None, kind: Incomplete | None = None, name: Incomplete | None = None, retry_after_seconds: Incomplete | None = None, uid: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def causes(self): ...
    @causes.setter
    def causes(self, causes) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def retry_after_seconds(self): ...
    @retry_after_seconds.setter
    def retry_after_seconds(self, retry_after_seconds) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

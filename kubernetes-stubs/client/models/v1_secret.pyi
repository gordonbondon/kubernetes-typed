# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1Secret:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, api_version: Any | None = ..., data: Any | None = ..., immutable: Any | None = ..., kind: Any | None = ..., metadata: Any | None = ..., string_data: Any | None = ..., type: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def data(self): ...
    @data.setter
    def data(self, data) -> None: ...
    @property
    def immutable(self): ...
    @immutable.setter
    def immutable(self, immutable) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata) -> None: ...
    @property
    def string_data(self): ...
    @string_data.setter
    def string_data(self, string_data) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1VolumeAttachmentSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, attacher: Any | None = ..., node_name: Any | None = ..., source: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def attacher(self): ...
    @attacher.setter
    def attacher(self, attacher) -> None: ...
    @property
    def node_name(self): ...
    @node_name.setter
    def node_name(self, node_name) -> None: ...
    @property
    def source(self): ...
    @source.setter
    def source(self, source) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

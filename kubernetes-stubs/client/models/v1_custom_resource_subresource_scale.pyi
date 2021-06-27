# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1CustomResourceSubresourceScale:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, label_selector_path: Any | None = ..., spec_replicas_path: Any | None = ..., status_replicas_path: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def label_selector_path(self): ...
    @label_selector_path.setter
    def label_selector_path(self, label_selector_path) -> None: ...
    @property
    def spec_replicas_path(self): ...
    @spec_replicas_path.setter
    def spec_replicas_path(self, spec_replicas_path) -> None: ...
    @property
    def status_replicas_path(self): ...
    @status_replicas_path.setter
    def status_replicas_path(self, status_replicas_path) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

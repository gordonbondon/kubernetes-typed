# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1TopologySpreadConstraint:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, label_selector: Any | None = ..., max_skew: Any | None = ..., topology_key: Any | None = ..., when_unsatisfiable: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def label_selector(self): ...
    @label_selector.setter
    def label_selector(self, label_selector) -> None: ...
    @property
    def max_skew(self): ...
    @max_skew.setter
    def max_skew(self, max_skew) -> None: ...
    @property
    def topology_key(self): ...
    @topology_key.setter
    def topology_key(self, topology_key) -> None: ...
    @property
    def when_unsatisfiable(self): ...
    @when_unsatisfiable.setter
    def when_unsatisfiable(self, when_unsatisfiable) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ClusterRole:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, aggregation_rule: Any | None = ..., api_version: Any | None = ..., kind: Any | None = ..., metadata: Any | None = ..., rules: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def aggregation_rule(self): ...
    @aggregation_rule.setter
    def aggregation_rule(self, aggregation_rule) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata) -> None: ...
    @property
    def rules(self): ...
    @rules.setter
    def rules(self, rules) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

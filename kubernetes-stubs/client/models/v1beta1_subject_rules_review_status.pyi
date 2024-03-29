# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1SubjectRulesReviewStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, evaluation_error: Any | None = ..., incomplete: Any | None = ..., non_resource_rules: Any | None = ..., resource_rules: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def evaluation_error(self): ...
    @evaluation_error.setter
    def evaluation_error(self, evaluation_error) -> None: ...
    @property
    def incomplete(self): ...
    @incomplete.setter
    def incomplete(self, incomplete) -> None: ...
    @property
    def non_resource_rules(self): ...
    @non_resource_rules.setter
    def non_resource_rules(self, non_resource_rules) -> None: ...
    @property
    def resource_rules(self): ...
    @resource_rules.setter
    def resource_rules(self, resource_rules) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1alpha1PolicyRulesWithSubjects:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, non_resource_rules: Incomplete | None = None, resource_rules: Incomplete | None = None, subjects: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def non_resource_rules(self): ...
    @non_resource_rules.setter
    def non_resource_rules(self, non_resource_rules) -> None: ...
    @property
    def resource_rules(self): ...
    @resource_rules.setter
    def resource_rules(self, resource_rules) -> None: ...
    @property
    def subjects(self): ...
    @subjects.setter
    def subjects(self, subjects) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

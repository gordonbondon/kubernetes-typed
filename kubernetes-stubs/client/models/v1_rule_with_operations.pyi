# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1RuleWithOperations:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, api_groups: Incomplete | None = None, api_versions: Incomplete | None = None, operations: Incomplete | None = None, resources: Incomplete | None = None, scope: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def api_groups(self): ...
    @api_groups.setter
    def api_groups(self, api_groups) -> None: ...
    @property
    def api_versions(self): ...
    @api_versions.setter
    def api_versions(self, api_versions) -> None: ...
    @property
    def operations(self): ...
    @operations.setter
    def operations(self, operations) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources) -> None: ...
    @property
    def scope(self): ...
    @scope.setter
    def scope(self, scope) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

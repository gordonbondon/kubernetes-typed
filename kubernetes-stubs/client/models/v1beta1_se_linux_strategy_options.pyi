# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1beta1SELinuxStrategyOptions:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, rule: Incomplete | None = None, se_linux_options: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def rule(self): ...
    @rule.setter
    def rule(self, rule) -> None: ...
    @property
    def se_linux_options(self): ...
    @se_linux_options.setter
    def se_linux_options(self, se_linux_options) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1SELinuxStrategyOptions:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, rule: Any | None = ..., se_linux_options: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
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

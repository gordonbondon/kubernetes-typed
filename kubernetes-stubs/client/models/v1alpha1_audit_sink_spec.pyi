# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1alpha1AuditSinkSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, policy: Any | None = ..., webhook: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def policy(self): ...
    @policy.setter
    def policy(self, policy) -> None: ...
    @property
    def webhook(self): ...
    @webhook.setter
    def webhook(self, webhook) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1DaemonSetSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, min_ready_seconds: Any | None = ..., revision_history_limit: Any | None = ..., selector: Any | None = ..., template: Any | None = ..., template_generation: Any | None = ..., update_strategy: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def min_ready_seconds(self): ...
    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds) -> None: ...
    @property
    def revision_history_limit(self): ...
    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector) -> None: ...
    @property
    def template(self): ...
    @template.setter
    def template(self, template) -> None: ...
    @property
    def template_generation(self): ...
    @template_generation.setter
    def template_generation(self, template_generation) -> None: ...
    @property
    def update_strategy(self): ...
    @update_strategy.setter
    def update_strategy(self, update_strategy) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

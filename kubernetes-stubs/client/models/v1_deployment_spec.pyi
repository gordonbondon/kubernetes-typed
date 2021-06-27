# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1DeploymentSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, min_ready_seconds: Any | None = ..., paused: Any | None = ..., progress_deadline_seconds: Any | None = ..., replicas: Any | None = ..., revision_history_limit: Any | None = ..., selector: Any | None = ..., strategy: Any | None = ..., template: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def min_ready_seconds(self): ...
    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds) -> None: ...
    @property
    def paused(self): ...
    @paused.setter
    def paused(self, paused) -> None: ...
    @property
    def progress_deadline_seconds(self): ...
    @progress_deadline_seconds.setter
    def progress_deadline_seconds(self, progress_deadline_seconds) -> None: ...
    @property
    def replicas(self): ...
    @replicas.setter
    def replicas(self, replicas) -> None: ...
    @property
    def revision_history_limit(self): ...
    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector) -> None: ...
    @property
    def strategy(self): ...
    @strategy.setter
    def strategy(self, strategy) -> None: ...
    @property
    def template(self): ...
    @template.setter
    def template(self, template) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

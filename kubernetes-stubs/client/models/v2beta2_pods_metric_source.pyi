# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V2beta2PodsMetricSource:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, metric: Incomplete | None = None, target: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def metric(self): ...
    @metric.setter
    def metric(self, metric) -> None: ...
    @property
    def target(self): ...
    @target.setter
    def target(self, target) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V2beta1PodsMetricSource:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, metric_name: Incomplete | None = None, selector: Incomplete | None = None, target_average_value: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def metric_name(self): ...
    @metric_name.setter
    def metric_name(self, metric_name) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector) -> None: ...
    @property
    def target_average_value(self): ...
    @target_average_value.setter
    def target_average_value(self, target_average_value) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

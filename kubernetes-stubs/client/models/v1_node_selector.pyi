# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1NodeSelector:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, node_selector_terms: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def node_selector_terms(self): ...
    @node_selector_terms.setter
    def node_selector_terms(self, node_selector_terms) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

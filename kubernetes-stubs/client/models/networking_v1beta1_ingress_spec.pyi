# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class NetworkingV1beta1IngressSpec:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, backend: Incomplete | None = None, ingress_class_name: Incomplete | None = None, rules: Incomplete | None = None, tls: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def backend(self): ...
    @backend.setter
    def backend(self, backend) -> None: ...
    @property
    def ingress_class_name(self): ...
    @ingress_class_name.setter
    def ingress_class_name(self, ingress_class_name) -> None: ...
    @property
    def rules(self): ...
    @rules.setter
    def rules(self, rules) -> None: ...
    @property
    def tls(self): ...
    @tls.setter
    def tls(self, tls) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class NetworkingV1beta1IngressBackend:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, resource: Incomplete | None = None, service_name: Incomplete | None = None, service_port: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def resource(self): ...
    @resource.setter
    def resource(self, resource) -> None: ...
    @property
    def service_name(self): ...
    @service_name.setter
    def service_name(self, service_name) -> None: ...
    @property
    def service_port(self): ...
    @service_port.setter
    def service_port(self, service_port) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class NetworkingV1beta1IngressTLS:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, hosts: Incomplete | None = None, secret_name: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def hosts(self): ...
    @hosts.setter
    def hosts(self, hosts) -> None: ...
    @property
    def secret_name(self): ...
    @secret_name.setter
    def secret_name(self, secret_name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

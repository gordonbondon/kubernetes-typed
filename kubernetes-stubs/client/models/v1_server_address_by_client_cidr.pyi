# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ServerAddressByClientCIDR:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, client_cidr: Incomplete | None = None, server_address: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def client_cidr(self): ...
    @client_cidr.setter
    def client_cidr(self, client_cidr) -> None: ...
    @property
    def server_address(self): ...
    @server_address.setter
    def server_address(self, server_address) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

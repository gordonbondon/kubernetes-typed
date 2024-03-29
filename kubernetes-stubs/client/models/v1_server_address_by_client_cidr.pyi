# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ServerAddressByClientCIDR:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, client_cidr: Any | None = ..., server_address: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
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

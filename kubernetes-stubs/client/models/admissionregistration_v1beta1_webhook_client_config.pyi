# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class AdmissionregistrationV1beta1WebhookClientConfig:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, ca_bundle: Incomplete | None = None, service: Incomplete | None = None, url: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def ca_bundle(self): ...
    @ca_bundle.setter
    def ca_bundle(self, ca_bundle) -> None: ...
    @property
    def service(self): ...
    @service.setter
    def service(self, service) -> None: ...
    @property
    def url(self): ...
    @url.setter
    def url(self, url) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

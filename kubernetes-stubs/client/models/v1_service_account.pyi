# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1ServiceAccount:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, api_version: Incomplete | None = None, automount_service_account_token: Incomplete | None = None, image_pull_secrets: Incomplete | None = None, kind: Incomplete | None = None, metadata: Incomplete | None = None, secrets: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def automount_service_account_token(self): ...
    @automount_service_account_token.setter
    def automount_service_account_token(self, automount_service_account_token) -> None: ...
    @property
    def image_pull_secrets(self): ...
    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata) -> None: ...
    @property
    def secrets(self): ...
    @secrets.setter
    def secrets(self, secrets) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

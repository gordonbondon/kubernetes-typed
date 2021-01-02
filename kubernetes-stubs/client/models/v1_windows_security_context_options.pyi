from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1WindowsSecurityContextOptions:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, gmsa_credential_spec: Optional[Any] = ..., gmsa_credential_spec_name: Optional[Any] = ..., run_as_user_name: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def gmsa_credential_spec(self): ...
    @gmsa_credential_spec.setter
    def gmsa_credential_spec(self, gmsa_credential_spec: Any) -> None: ...
    @property
    def gmsa_credential_spec_name(self): ...
    @gmsa_credential_spec_name.setter
    def gmsa_credential_spec_name(self, gmsa_credential_spec_name: Any) -> None: ...
    @property
    def run_as_user_name(self): ...
    @run_as_user_name.setter
    def run_as_user_name(self, run_as_user_name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

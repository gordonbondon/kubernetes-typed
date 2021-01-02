from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1alpha1RoleBinding:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, api_version: Optional[Any] = ..., kind: Optional[Any] = ..., metadata: Optional[Any] = ..., role_ref: Optional[Any] = ..., subjects: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata: Any) -> None: ...
    @property
    def role_ref(self): ...
    @role_ref.setter
    def role_ref(self, role_ref: Any) -> None: ...
    @property
    def subjects(self): ...
    @subjects.setter
    def subjects(self, subjects: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

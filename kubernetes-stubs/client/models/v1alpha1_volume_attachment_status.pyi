# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1alpha1VolumeAttachmentStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, attach_error: Optional[Any] = ..., attached: Optional[Any] = ..., attachment_metadata: Optional[Any] = ..., detach_error: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def attach_error(self): ...
    @attach_error.setter
    def attach_error(self, attach_error: Any) -> None: ...
    @property
    def attached(self): ...
    @attached.setter
    def attached(self, attached: Any) -> None: ...
    @property
    def attachment_metadata(self): ...
    @attachment_metadata.setter
    def attachment_metadata(self, attachment_metadata: Any) -> None: ...
    @property
    def detach_error(self): ...
    @detach_error.setter
    def detach_error(self, detach_error: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

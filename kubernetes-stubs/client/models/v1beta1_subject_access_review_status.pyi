# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1beta1SubjectAccessReviewStatus:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, allowed: Incomplete | None = None, denied: Incomplete | None = None, evaluation_error: Incomplete | None = None, reason: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def allowed(self): ...
    @allowed.setter
    def allowed(self, allowed) -> None: ...
    @property
    def denied(self): ...
    @denied.setter
    def denied(self, denied) -> None: ...
    @property
    def evaluation_error(self): ...
    @evaluation_error.setter
    def evaluation_error(self, evaluation_error) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1beta1ValidatingWebhook:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, admission_review_versions: Incomplete | None = None, client_config: Incomplete | None = None, failure_policy: Incomplete | None = None, match_policy: Incomplete | None = None, name: Incomplete | None = None, namespace_selector: Incomplete | None = None, object_selector: Incomplete | None = None, rules: Incomplete | None = None, side_effects: Incomplete | None = None, timeout_seconds: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def admission_review_versions(self): ...
    @admission_review_versions.setter
    def admission_review_versions(self, admission_review_versions) -> None: ...
    @property
    def client_config(self): ...
    @client_config.setter
    def client_config(self, client_config) -> None: ...
    @property
    def failure_policy(self): ...
    @failure_policy.setter
    def failure_policy(self, failure_policy) -> None: ...
    @property
    def match_policy(self): ...
    @match_policy.setter
    def match_policy(self, match_policy) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def namespace_selector(self): ...
    @namespace_selector.setter
    def namespace_selector(self, namespace_selector) -> None: ...
    @property
    def object_selector(self): ...
    @object_selector.setter
    def object_selector(self, object_selector) -> None: ...
    @property
    def rules(self): ...
    @rules.setter
    def rules(self, rules) -> None: ...
    @property
    def side_effects(self): ...
    @side_effects.setter
    def side_effects(self, side_effects) -> None: ...
    @property
    def timeout_seconds(self): ...
    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

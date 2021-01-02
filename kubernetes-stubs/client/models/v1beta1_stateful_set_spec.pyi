from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1StatefulSetSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, pod_management_policy: Optional[Any] = ..., replicas: Optional[Any] = ..., revision_history_limit: Optional[Any] = ..., selector: Optional[Any] = ..., service_name: Optional[Any] = ..., template: Optional[Any] = ..., update_strategy: Optional[Any] = ..., volume_claim_templates: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def pod_management_policy(self): ...
    @pod_management_policy.setter
    def pod_management_policy(self, pod_management_policy: Any) -> None: ...
    @property
    def replicas(self): ...
    @replicas.setter
    def replicas(self, replicas: Any) -> None: ...
    @property
    def revision_history_limit(self): ...
    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    @property
    def service_name(self): ...
    @service_name.setter
    def service_name(self, service_name: Any) -> None: ...
    @property
    def template(self): ...
    @template.setter
    def template(self, template: Any) -> None: ...
    @property
    def update_strategy(self): ...
    @update_strategy.setter
    def update_strategy(self, update_strategy: Any) -> None: ...
    @property
    def volume_claim_templates(self): ...
    @volume_claim_templates.setter
    def volume_claim_templates(self, volume_claim_templates: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

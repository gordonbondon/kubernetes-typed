# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1beta1Event:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, action: Incomplete | None = None, api_version: Incomplete | None = None, deprecated_count: Incomplete | None = None, deprecated_first_timestamp: Incomplete | None = None, deprecated_last_timestamp: Incomplete | None = None, deprecated_source: Incomplete | None = None, event_time: Incomplete | None = None, kind: Incomplete | None = None, metadata: Incomplete | None = None, note: Incomplete | None = None, reason: Incomplete | None = None, regarding: Incomplete | None = None, related: Incomplete | None = None, reporting_controller: Incomplete | None = None, reporting_instance: Incomplete | None = None, series: Incomplete | None = None, type: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def action(self): ...
    @action.setter
    def action(self, action) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def deprecated_count(self): ...
    @deprecated_count.setter
    def deprecated_count(self, deprecated_count) -> None: ...
    @property
    def deprecated_first_timestamp(self): ...
    @deprecated_first_timestamp.setter
    def deprecated_first_timestamp(self, deprecated_first_timestamp) -> None: ...
    @property
    def deprecated_last_timestamp(self): ...
    @deprecated_last_timestamp.setter
    def deprecated_last_timestamp(self, deprecated_last_timestamp) -> None: ...
    @property
    def deprecated_source(self): ...
    @deprecated_source.setter
    def deprecated_source(self, deprecated_source) -> None: ...
    @property
    def event_time(self): ...
    @event_time.setter
    def event_time(self, event_time) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata) -> None: ...
    @property
    def note(self): ...
    @note.setter
    def note(self, note) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason) -> None: ...
    @property
    def regarding(self): ...
    @regarding.setter
    def regarding(self, regarding) -> None: ...
    @property
    def related(self): ...
    @related.setter
    def related(self, related) -> None: ...
    @property
    def reporting_controller(self): ...
    @reporting_controller.setter
    def reporting_controller(self, reporting_controller) -> None: ...
    @property
    def reporting_instance(self): ...
    @reporting_instance.setter
    def reporting_instance(self, reporting_instance) -> None: ...
    @property
    def series(self): ...
    @series.setter
    def series(self, series) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

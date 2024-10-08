# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V1NodeSystemInfo:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, architecture: Incomplete | None = None, boot_id: Incomplete | None = None, container_runtime_version: Incomplete | None = None, kernel_version: Incomplete | None = None, kube_proxy_version: Incomplete | None = None, kubelet_version: Incomplete | None = None, machine_id: Incomplete | None = None, operating_system: Incomplete | None = None, os_image: Incomplete | None = None, system_uuid: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def architecture(self): ...
    @architecture.setter
    def architecture(self, architecture) -> None: ...
    @property
    def boot_id(self): ...
    @boot_id.setter
    def boot_id(self, boot_id) -> None: ...
    @property
    def container_runtime_version(self): ...
    @container_runtime_version.setter
    def container_runtime_version(self, container_runtime_version) -> None: ...
    @property
    def kernel_version(self): ...
    @kernel_version.setter
    def kernel_version(self, kernel_version) -> None: ...
    @property
    def kube_proxy_version(self): ...
    @kube_proxy_version.setter
    def kube_proxy_version(self, kube_proxy_version) -> None: ...
    @property
    def kubelet_version(self): ...
    @kubelet_version.setter
    def kubelet_version(self, kubelet_version) -> None: ...
    @property
    def machine_id(self): ...
    @machine_id.setter
    def machine_id(self, machine_id) -> None: ...
    @property
    def operating_system(self): ...
    @operating_system.setter
    def operating_system(self, operating_system) -> None: ...
    @property
    def os_image(self): ...
    @os_image.setter
    def os_image(self, os_image) -> None: ...
    @property
    def system_uuid(self): ...
    @system_uuid.setter
    def system_uuid(self, system_uuid) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

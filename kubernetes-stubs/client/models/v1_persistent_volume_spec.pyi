# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1PersistentVolumeSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, access_modes: Any | None = ..., aws_elastic_block_store: Any | None = ..., azure_disk: Any | None = ..., azure_file: Any | None = ..., capacity: Any | None = ..., cephfs: Any | None = ..., cinder: Any | None = ..., claim_ref: Any | None = ..., csi: Any | None = ..., fc: Any | None = ..., flex_volume: Any | None = ..., flocker: Any | None = ..., gce_persistent_disk: Any | None = ..., glusterfs: Any | None = ..., host_path: Any | None = ..., iscsi: Any | None = ..., local: Any | None = ..., mount_options: Any | None = ..., nfs: Any | None = ..., node_affinity: Any | None = ..., persistent_volume_reclaim_policy: Any | None = ..., photon_persistent_disk: Any | None = ..., portworx_volume: Any | None = ..., quobyte: Any | None = ..., rbd: Any | None = ..., scale_io: Any | None = ..., storage_class_name: Any | None = ..., storageos: Any | None = ..., volume_mode: Any | None = ..., vsphere_volume: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def access_modes(self): ...
    @access_modes.setter
    def access_modes(self, access_modes) -> None: ...
    @property
    def aws_elastic_block_store(self): ...
    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, aws_elastic_block_store) -> None: ...
    @property
    def azure_disk(self): ...
    @azure_disk.setter
    def azure_disk(self, azure_disk) -> None: ...
    @property
    def azure_file(self): ...
    @azure_file.setter
    def azure_file(self, azure_file) -> None: ...
    @property
    def capacity(self): ...
    @capacity.setter
    def capacity(self, capacity) -> None: ...
    @property
    def cephfs(self): ...
    @cephfs.setter
    def cephfs(self, cephfs) -> None: ...
    @property
    def cinder(self): ...
    @cinder.setter
    def cinder(self, cinder) -> None: ...
    @property
    def claim_ref(self): ...
    @claim_ref.setter
    def claim_ref(self, claim_ref) -> None: ...
    @property
    def csi(self): ...
    @csi.setter
    def csi(self, csi) -> None: ...
    @property
    def fc(self): ...
    @fc.setter
    def fc(self, fc) -> None: ...
    @property
    def flex_volume(self): ...
    @flex_volume.setter
    def flex_volume(self, flex_volume) -> None: ...
    @property
    def flocker(self): ...
    @flocker.setter
    def flocker(self, flocker) -> None: ...
    @property
    def gce_persistent_disk(self): ...
    @gce_persistent_disk.setter
    def gce_persistent_disk(self, gce_persistent_disk) -> None: ...
    @property
    def glusterfs(self): ...
    @glusterfs.setter
    def glusterfs(self, glusterfs) -> None: ...
    @property
    def host_path(self): ...
    @host_path.setter
    def host_path(self, host_path) -> None: ...
    @property
    def iscsi(self): ...
    @iscsi.setter
    def iscsi(self, iscsi) -> None: ...
    @property
    def local(self): ...
    @local.setter
    def local(self, local) -> None: ...
    @property
    def mount_options(self): ...
    @mount_options.setter
    def mount_options(self, mount_options) -> None: ...
    @property
    def nfs(self): ...
    @nfs.setter
    def nfs(self, nfs) -> None: ...
    @property
    def node_affinity(self): ...
    @node_affinity.setter
    def node_affinity(self, node_affinity) -> None: ...
    @property
    def persistent_volume_reclaim_policy(self): ...
    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, persistent_volume_reclaim_policy) -> None: ...
    @property
    def photon_persistent_disk(self): ...
    @photon_persistent_disk.setter
    def photon_persistent_disk(self, photon_persistent_disk) -> None: ...
    @property
    def portworx_volume(self): ...
    @portworx_volume.setter
    def portworx_volume(self, portworx_volume) -> None: ...
    @property
    def quobyte(self): ...
    @quobyte.setter
    def quobyte(self, quobyte) -> None: ...
    @property
    def rbd(self): ...
    @rbd.setter
    def rbd(self, rbd) -> None: ...
    @property
    def scale_io(self): ...
    @scale_io.setter
    def scale_io(self, scale_io) -> None: ...
    @property
    def storage_class_name(self): ...
    @storage_class_name.setter
    def storage_class_name(self, storage_class_name) -> None: ...
    @property
    def storageos(self): ...
    @storageos.setter
    def storageos(self, storageos) -> None: ...
    @property
    def volume_mode(self): ...
    @volume_mode.setter
    def volume_mode(self, volume_mode) -> None: ...
    @property
    def vsphere_volume(self): ...
    @vsphere_volume.setter
    def vsphere_volume(self, vsphere_volume) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

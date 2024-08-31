# Code generated by `stubgen`. DO NOT EDIT.
import abc
import json
from .exceptions import ApiException as ApiException, NotFoundError as NotFoundError, ResourceNotFoundError as ResourceNotFoundError, ResourceNotUniqueError as ResourceNotUniqueError, ServiceUnavailableError as ServiceUnavailableError
from .resource import Resource as Resource, ResourceList as ResourceList
from _typeshed import Incomplete
from abc import abstractmethod
from kubernetes import __version__ as __version__

DISCOVERY_PREFIX: str

class Discoverer(metaclass=abc.ABCMeta):
    client: Incomplete
    def __init__(self, client, cache_file) -> None: ...
    def invalidate_cache(self) -> None: ...
    @property
    @abc.abstractmethod
    def api_groups(self): ...
    @abstractmethod
    def search(self, prefix: Incomplete | None = None, group: Incomplete | None = None, api_version: Incomplete | None = None, kind: Incomplete | None = None, **kwargs): ...
    @abstractmethod
    def discover(self): ...
    @property
    def version(self): ...
    def default_groups(self, request_resources: bool = False): ...
    def parse_api_groups(self, request_resources: bool = False, update: bool = False): ...
    def get_resources_for_api_version(self, prefix, group, version, preferred): ...
    def get(self, **kwargs): ...

class LazyDiscoverer(Discoverer):
    def __init__(self, client, cache_file) -> None: ...
    def discover(self) -> None: ...
    @property
    def api_groups(self): ...
    def search(self, **kwargs): ...
    def __iter__(self): ...

class EagerDiscoverer(Discoverer):
    def update(self, resources) -> None: ...
    def __init__(self, client, cache_file) -> None: ...
    def discover(self) -> None: ...
    @property
    def api_groups(self): ...
    def search(self, **kwargs): ...
    def __iter__(self): ...

class ResourceGroup:
    preferred: Incomplete
    resources: Incomplete
    def __init__(self, preferred, resources: Incomplete | None = None) -> None: ...
    def to_dict(self): ...

class CacheEncoder(json.JSONEncoder):
    def default(self, o): ...

class CacheDecoder(json.JSONDecoder):
    client: Incomplete
    def __init__(self, client, *args, **kwargs) -> None: ...
    def object_hook(self, obj): ...
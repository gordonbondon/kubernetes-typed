# Code generated by `stubgen`. DO NOT EDIT.
from .discovery import EagerDiscoverer as EagerDiscoverer, LazyDiscoverer as LazyDiscoverer
from .resource import Resource as Resource, ResourceField as ResourceField, ResourceInstance as ResourceInstance, ResourceList as ResourceList, Subresource as Subresource
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['DynamicClient', 'ResourceInstance', 'Resource', 'ResourceList', 'Subresource', 'EagerDiscoverer', 'LazyDiscoverer', 'ResourceField']

class VersionNotSupportedError(NotImplementedError): ...

class DynamicClient:
    client: Incomplete
    configuration: Incomplete
    def __init__(self, client, cache_file: Incomplete | None = None, discoverer: Incomplete | None = None) -> None: ...
    @property
    def resources(self): ...
    @property
    def version(self): ...
    def ensure_namespace(self, resource, namespace, body): ...
    def serialize_body(self, body): ...
    def get(self, resource, name: Incomplete | None = None, namespace: Incomplete | None = None, **kwargs): ...
    def create(self, resource, body: Incomplete | None = None, namespace: Incomplete | None = None, **kwargs): ...
    def delete(self, resource, name: Incomplete | None = None, namespace: Incomplete | None = None, body: Incomplete | None = None, label_selector: Incomplete | None = None, field_selector: Incomplete | None = None, **kwargs): ...
    def replace(self, resource, body: Incomplete | None = None, name: Incomplete | None = None, namespace: Incomplete | None = None, **kwargs): ...
    def patch(self, resource, body: Incomplete | None = None, name: Incomplete | None = None, namespace: Incomplete | None = None, **kwargs): ...
    def watch(self, resource, namespace: Incomplete | None = None, name: Incomplete | None = None, label_selector: Incomplete | None = None, field_selector: Incomplete | None = None, resource_version: Incomplete | None = None, timeout: Incomplete | None = None, watcher: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def request(self, method, path, body: Incomplete | None = None, **params): ...
    def validate(self, definition, version: Incomplete | None = None, strict: bool = False): ...
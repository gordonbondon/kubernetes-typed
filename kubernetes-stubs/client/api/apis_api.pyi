# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError

class ApisApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def get_api_versions(self, **kwargs): ...
    def get_api_versions_with_http_info(self, **kwargs): ...

# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any

class AuthorizationApi:
    api_client: Any
    def __init__(self, api_client: Any | None = ...) -> None: ...
    def get_api_group(self, **kwargs): ...
    def get_api_group_with_http_info(self, **kwargs): ...

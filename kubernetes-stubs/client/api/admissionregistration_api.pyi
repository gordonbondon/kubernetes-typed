# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError

class AdmissionregistrationApi:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def get_api_group(self, **kwargs): ...
    def get_api_group_with_http_info(self, **kwargs): ...

# Code generated by `stubgen`. DO NOT EDIT.
import io
from kubernetes.client.exceptions import ApiException as ApiException, ApiValueError as ApiValueError
from typing import Any

logger: Any

class RESTResponse(io.IOBase):
    urllib3_response: Any
    status: Any
    reason: Any
    data: Any
    def __init__(self, resp) -> None: ...
    def getheaders(self): ...
    def getheader(self, name, default: Any | None = ...): ...

class RESTClientObject:
    pool_manager: Any
    def __init__(self, configuration, pools_size: int = ..., maxsize: Any | None = ...) -> None: ...
    def request(self, method, url, query_params: Any | None = ..., headers: Any | None = ..., body: Any | None = ..., post_params: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...
    def GET(self, url, headers: Any | None = ..., query_params: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...
    def HEAD(self, url, headers: Any | None = ..., query_params: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...
    def OPTIONS(self, url, headers: Any | None = ..., query_params: Any | None = ..., post_params: Any | None = ..., body: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...
    def DELETE(self, url, headers: Any | None = ..., query_params: Any | None = ..., body: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...
    def POST(self, url, headers: Any | None = ..., query_params: Any | None = ..., post_params: Any | None = ..., body: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...
    def PUT(self, url, headers: Any | None = ..., query_params: Any | None = ..., post_params: Any | None = ..., body: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...
    def PATCH(self, url, headers: Any | None = ..., query_params: Any | None = ..., post_params: Any | None = ..., body: Any | None = ..., _preload_content: bool = ..., _request_timeout: Any | None = ...): ...

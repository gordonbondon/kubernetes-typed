# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.rest import ApiException as ApiException, ApiValueError as ApiValueError
from typing import Any, NamedTuple

STDIN_CHANNEL: int
STDOUT_CHANNEL: int
STDERR_CHANNEL: int
ERROR_CHANNEL: int
RESIZE_CHANNEL: int

class _IgnoredIO:
    def write(self, _x) -> None: ...
    def getvalue(self) -> None: ...

class WSClient:
    sock: Any
    def __init__(self, configuration, url, headers, capture_all) -> None: ...
    def peek_channel(self, channel, timeout: int = ...): ...
    def read_channel(self, channel, timeout: int = ...): ...
    def readline_channel(self, channel, timeout: Any | None = ...): ...
    def write_channel(self, channel, data) -> None: ...
    def peek_stdout(self, timeout: int = ...): ...
    def read_stdout(self, timeout: Any | None = ...): ...
    def readline_stdout(self, timeout: Any | None = ...): ...
    def peek_stderr(self, timeout: int = ...): ...
    def read_stderr(self, timeout: Any | None = ...): ...
    def readline_stderr(self, timeout: Any | None = ...): ...
    def read_all(self): ...
    def is_open(self): ...
    def write_stdin(self, data) -> None: ...
    def update(self, timeout: int = ...) -> None: ...
    def run_forever(self, timeout: Any | None = ...) -> None: ...
    @property
    def returncode(self): ...
    def close(self, **kwargs) -> None: ...

class WSResponse(NamedTuple):
    data: Any

class PortForward:
    websocket: Any
    local_ports: Any
    def __init__(self, websocket, ports) -> None: ...
    @property
    def connected(self): ...
    def socket(self, port_number): ...
    def error(self, port_number): ...
    def close(self) -> None: ...
    class _Port:
        port_number: Any
        channel: Any
        socket: Any
        data: bytes
        error: Any
        def __init__(self, ix, port_number) -> None: ...
        class _Socket:
            def __init__(self, socket) -> None: ...
            def __getattr__(self, name): ...
            def setsockopt(self, level, optname, value) -> None: ...

def get_websocket_url(url, query_params: Any | None = ...): ...
def create_websocket(configuration, url, headers: Any | None = ...): ...
def websocket_call(configuration, _method, url, **kwargs): ...
def portforward_call(configuration, _method, url, **kwargs): ...

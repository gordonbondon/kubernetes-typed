# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.rest import ApiException as ApiException, ApiValueError as ApiValueError
from typing import NamedTuple

STDIN_CHANNEL: int
STDOUT_CHANNEL: int
STDERR_CHANNEL: int
ERROR_CHANNEL: int
RESIZE_CHANNEL: int

class _IgnoredIO:
    def write(self, _x) -> None: ...
    def getvalue(self) -> None: ...

class WSClient:
    sock: Incomplete
    def __init__(self, configuration, url, headers, capture_all) -> None: ...
    def peek_channel(self, channel, timeout: int = 0): ...
    def read_channel(self, channel, timeout: int = 0): ...
    def readline_channel(self, channel, timeout: Incomplete | None = None): ...
    def write_channel(self, channel, data) -> None: ...
    def peek_stdout(self, timeout: int = 0): ...
    def read_stdout(self, timeout: Incomplete | None = None): ...
    def readline_stdout(self, timeout: Incomplete | None = None): ...
    def peek_stderr(self, timeout: int = 0): ...
    def read_stderr(self, timeout: Incomplete | None = None): ...
    def readline_stderr(self, timeout: Incomplete | None = None): ...
    def read_all(self): ...
    def is_open(self): ...
    def write_stdin(self, data) -> None: ...
    def update(self, timeout: int = 0) -> None: ...
    def run_forever(self, timeout: Incomplete | None = None) -> None: ...
    @property
    def returncode(self): ...
    def close(self, **kwargs) -> None: ...

class WSResponse(NamedTuple):
    data: Incomplete

class PortForward:
    websocket: Incomplete
    local_ports: Incomplete
    def __init__(self, websocket, ports) -> None: ...
    @property
    def connected(self): ...
    def socket(self, port_number): ...
    def error(self, port_number): ...
    def close(self) -> None: ...
    class _Port:
        port_number: Incomplete
        channel: Incomplete
        socket: Incomplete
        data: bytes
        error: Incomplete
        def __init__(self, ix, port_number) -> None: ...
        class _Socket:
            def __init__(self, socket) -> None: ...
            def __getattr__(self, name): ...
            def setsockopt(self, level, optname, value) -> None: ...

def get_websocket_url(url, query_params: Incomplete | None = None): ...
def create_websocket(configuration, url, headers: Incomplete | None = None): ...
def websocket_call(configuration, _method, url, **kwargs): ...
def portforward_call(configuration, _method, url, **kwargs): ...

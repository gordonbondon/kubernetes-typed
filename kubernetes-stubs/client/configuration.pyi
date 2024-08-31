# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete

class Configuration:
    host: Incomplete
    temp_folder_path: Incomplete
    api_key: Incomplete
    api_key_prefix: Incomplete
    refresh_api_key_hook: Incomplete
    username: Incomplete
    password: Incomplete
    discard_unknown_keys: Incomplete
    logger: Incomplete
    logger_stream_handler: Incomplete
    logger_file_handler: Incomplete
    verify_ssl: bool
    ssl_ca_cert: Incomplete
    cert_file: Incomplete
    key_file: Incomplete
    assert_hostname: Incomplete
    connection_pool_maxsize: Incomplete
    proxy: Incomplete
    proxy_headers: Incomplete
    safe_chars_for_path_param: str
    retries: Incomplete
    client_side_validation: bool
    def __init__(self, host: str = 'http://localhost', api_key: Incomplete | None = None, api_key_prefix: Incomplete | None = None, username: Incomplete | None = None, password: Incomplete | None = None, discard_unknown_keys: bool = False) -> None: ...
    def __deepcopy__(self, memo): ...
    @classmethod
    def set_default(cls, default) -> None: ...
    @classmethod
    def get_default_copy(cls): ...
    @property
    def logger_file(self): ...
    @logger_file.setter
    def logger_file(self, value) -> None: ...
    @property
    def debug(self): ...
    @debug.setter
    def debug(self, value) -> None: ...
    @property
    def logger_format(self): ...
    logger_formatter: Incomplete
    @logger_format.setter
    def logger_format(self, value) -> None: ...
    def get_api_key_with_prefix(self, identifier): ...
    def get_basic_auth_token(self): ...
    def auth_settings(self): ...
    def to_debug_report(self): ...
    def get_host_settings(self): ...
    def get_host_from_settings(self, index, variables: Incomplete | None = None): ...

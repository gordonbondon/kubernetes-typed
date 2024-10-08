# Code generated by `stubgen`. DO NOT EDIT.
from .config_exception import ConfigException as ConfigException
from _typeshed import Incomplete
from kubernetes.client import Configuration as Configuration

SERVICE_HOST_ENV_NAME: str
SERVICE_PORT_ENV_NAME: str
SERVICE_TOKEN_FILENAME: str
SERVICE_CERT_FILENAME: str

class InClusterConfigLoader:
    def __init__(self, token_filename, cert_filename, try_refresh_token: bool = True, environ=...) -> None: ...
    def load_and_set(self, client_configuration: Incomplete | None = None) -> None: ...

def load_incluster_config(client_configuration: Incomplete | None = None, try_refresh_token: bool = True) -> None: ...

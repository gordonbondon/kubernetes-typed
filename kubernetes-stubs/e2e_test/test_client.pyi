# Code generated by `stubgen`. DO NOT EDIT.
import unittest
from kubernetes.client import api_client as api_client
from kubernetes.client.api import core_v1_api as core_v1_api
from kubernetes.e2e_test import base as base
from kubernetes.stream import portforward as portforward, stream as stream
from kubernetes.stream.ws_client import ERROR_CHANNEL as ERROR_CHANNEL

def short_uuid(): ...
def manifest_with_command(name, command): ...

class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_pod_apis(self) -> None: ...
    def test_exit_code(self) -> None: ...
    def test_portforward_raw(self) -> None: ...
    def test_portforward_http(self): ...
    def test_service_apis(self) -> None: ...
    def test_replication_controller_apis(self) -> None: ...
    def test_configmap_apis(self) -> None: ...
    def test_node_apis(self) -> None: ...

# Code generated by `stubgen`. DO NOT EDIT.
import unittest
from kubernetes.client import api_client as api_client
from kubernetes.client.api import apps_v1_api as apps_v1_api
from kubernetes.client.models import v1_delete_options as v1_delete_options
from kubernetes.e2e_test import base as base

class TestClientApps(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_create_deployment(self) -> None: ...
    def test_create_daemonset(self) -> None: ...

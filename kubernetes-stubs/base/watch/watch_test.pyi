# Code generated by `stubgen`. DO NOT EDIT.
import unittest
from .watch import Watch as Watch
from kubernetes import client as client

class WatchTests(unittest.TestCase):
    callcount: int
    def setUp(self) -> None: ...
    def test_watch_with_decode(self) -> None: ...
    def test_watch_for_follow(self) -> None: ...
    def test_watch_resource_version_set(self): ...
    def test_watch_stream_twice(self) -> None: ...
    def test_watch_stream_loop(self) -> None: ...
    def test_unmarshal_with_float_object(self) -> None: ...
    def test_unmarshal_with_no_return_type(self) -> None: ...
    def test_unmarshal_with_custom_object(self) -> None: ...
    def test_unmarshal_with_bookmark(self) -> None: ...
    def test_watch_with_exception(self) -> None: ...
    def test_watch_with_error_event(self) -> None: ...
    def test_watch_retries_on_error_event(self) -> None: ...
    def test_watch_with_error_event_and_timeout_param(self) -> None: ...
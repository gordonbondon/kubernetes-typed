# Code generated by `stubgen`. DO NOT EDIT.
import datetime
from typing import Any

class TimezoneInfo(datetime.tzinfo):
    def __init__(self, h, m) -> None: ...
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...

UTC: Any
MICROSEC_PER_SEC: int

def parse_rfc3339(s): ...
def format_rfc3339(date_time): ...

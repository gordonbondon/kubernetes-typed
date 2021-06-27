# Code generated by `stubgen`. DO NOT EDIT.
from .leaderelectionrecord import LeaderElectionRecord as LeaderElectionRecord
from typing import Any

class LeaderElection:
    observed_record: Any
    election_config: Any
    observed_time_milliseconds: int
    def __init__(self, election_config) -> None: ...
    def run(self) -> None: ...
    def acquire(self): ...
    def renew_loop(self) -> None: ...
    def try_acquire_or_renew(self): ...
    def update_lock(self, leader_election_record): ...

# Code generated by `stubgen`. DO NOT EDIT.
from _typeshed import Incomplete
from kubernetes.client.configuration import Configuration as Configuration

class V2alpha1CronJobSpec:
    openapi_types: Incomplete
    attribute_map: Incomplete
    local_vars_configuration: Incomplete
    discriminator: Incomplete
    def __init__(self, concurrency_policy: Incomplete | None = None, failed_jobs_history_limit: Incomplete | None = None, job_template: Incomplete | None = None, schedule: Incomplete | None = None, starting_deadline_seconds: Incomplete | None = None, successful_jobs_history_limit: Incomplete | None = None, suspend: Incomplete | None = None, local_vars_configuration: Incomplete | None = None) -> None: ...
    @property
    def concurrency_policy(self): ...
    @concurrency_policy.setter
    def concurrency_policy(self, concurrency_policy) -> None: ...
    @property
    def failed_jobs_history_limit(self): ...
    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, failed_jobs_history_limit) -> None: ...
    @property
    def job_template(self): ...
    @job_template.setter
    def job_template(self, job_template) -> None: ...
    @property
    def schedule(self): ...
    @schedule.setter
    def schedule(self, schedule) -> None: ...
    @property
    def starting_deadline_seconds(self): ...
    @starting_deadline_seconds.setter
    def starting_deadline_seconds(self, starting_deadline_seconds) -> None: ...
    @property
    def successful_jobs_history_limit(self): ...
    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, successful_jobs_history_limit) -> None: ...
    @property
    def suspend(self): ...
    @suspend.setter
    def suspend(self, suspend) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

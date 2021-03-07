from typing import TYPE_CHECKING

from kubernetes import client
from kubernetes.client.configuration import Configuration

conf = Configuration()
conf.client_side_validation = False

container = client.V1Container(name="pi", image="perl", command=["perl"], local_vars_configuration=conf)

template = client.V1PodTemplateSpec(
    metadata=client.V1ObjectMeta(labels={"app": "pi"}),
    spec=client.V1PodSpec(restart_policy="Never", containers=[container]),
)

spec = client.V1JobSpec(template=template, backoff_limit=4)

job = client.V1Job(
    api_version="batch/v1",
    kind="Job",
    metadata=client.V1ObjectMeta(name="pi"),
    spec=spec,
)

if TYPE_CHECKING:
    reveal_type(job.spec.template.spec)
    reveal_type(job.spec.template.spec.containers[0].image)

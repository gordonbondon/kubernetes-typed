from typing import TYPE_CHECKING

from kubernetes.client.api import core_v1_api

from kubernetes_typed.client import V1PodDict

api_instance = core_v1_api.CoreV1Api()

pod_manifest: V1PodDict = {
    "api_version": "v1",
    "kind": "Pod",
    "metadata": {"name": "test-pod"},
    "spec": {
        "containers": [
            {
                "image": "nginx",
                "name": "nginx",
            },
        ],
    },
}

if TYPE_CHECKING:
    reveal_type(pod_manifest["kind"])

pod_manifest["spec"]["containers"][0]["name"] = 1

api_instance.create_namespaced_pod(body=pod_manifest, namespace="default")

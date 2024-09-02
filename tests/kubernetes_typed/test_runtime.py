from kubernetes.client.api import core_v1_api

from kubernetes_typed.client import V1PodDict


def test_runtime():
    """Check that dict imports work at runtime."""

    pod_manifest: V1PodDict = {
        "apiVersion": "v1",
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

    pod_manifest["spec"]["containers"][0]["name"] = "new-nginx"

    assert pod_manifest["spec"]["containers"][0]["name"] == "new-nginx"

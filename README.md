<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>

# kubernetes-typed

[![Build status](https://github.com/gordonbondon/kubernetes-typed/workflows/Test/badge.svg?branch=master&event=push)](https://github.com/gordonbondon/kubernetes-typed/actions?query=workflow%3ATest+branch%3Amaster)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

mypy plugin to dynamically define types for Kubernetes objects.

## Features

* [Type checking for Custom Resources](#Custom-Resource-Definitions)
* [Type checking for kubernetes-client](#Kubernetes-Python-Client-types)

## Installation

Install with `pip`:
```shell
pip install kubernetes-typed
```

### Versioning

This package follows `kubernetes` client [versioning approach](https://github.com/kubernetes-client/python#homogenizing-the-kubernetes-python-client-versions).
`MAJOR.MINOR` parts of version will match client version for which stubs were generated, and `PATCH` version will be stub or plugin specific updates.

## Custom Resource Definitions

Add type checks for [Custom Resource Definition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) spec given its definition in `yaml` file .

1. Configure `mypy` to use `crd_typed` plugin:
```ini
[mypy]

plugins = crd_typed.plugin
```

2. Import `CustomResource`

```python
from crd_type import CustomResource
```

3. [Annotate](https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html#explicit-types-for-variables) your variables:

```python
resource: CustomResource["relative/path/to/crd.yaml"]
```

You can get type definition for different parts of crd:

* Get `TypeDict` definition for custom resource body:

    ```python
    from crd_type import CustomResource

    resource: CustomResource["relative/path/to/crd.yaml"]
    ```

* Get definition only for resource `spec`:

    ```python
    from crd_type import CustomResource

    resource: CustomResource["relative/path/to/crd.yaml", "spec"]
    ```

* Get definition for nested spec item, if that item is type `object` or `array`:

    ```python
    from crd_type import CustomResource

    resource: CustomResource["relative/path/to/crd.yaml", "spec", "some_property"]
    ```

* Get definition for array item, if that is array of objects, via `items` key:

    ```python
    from crd_type import CustomResource

    resource: CustomResource["relative/path/to/crd.yaml", "spec", "some_array_of_objects", "items"]
    ```

### Limitations

* CRDs that use `additionalProperties` are not supported.
* CRDs can define multiple `versions`, currently only first one will be used
* Custom attributes like `x-kubernetes-int-or-string`, `x-kubernetes-embedded-resource`, are not supported

## Kubernetes Python Client types

This package provides basic [type stubs](https://www.python.org/dev/peps/pep-0561/) for [kubernetes python client](https://github.com/kubernetes-client/python) out of the box.

To enable full type checking for classes use provided `kubernetes_typed` plugin. This plugin requires `kubernetes`, you can require it during installation like this:

```shell
pip install kubernetes-typed[client]
```

Configure `mypy` to use it and it will automatically type check classes from `kubernetes.client`:

```ini
[mypy]

plugins = kubernetes_typed.plugin
```

### Kubernetes Python Client Models Dict Types

If you want to type check resource dicts instead of classes, you can use generated `TypedDict`s provided by this package.

To do this for any model class in `kubernetes.client` append its name with `Dict`, and import it from `kubernetes_type.client`

For example:

`kubernetes.client.V1Pod` -> `kubernetes_typed.client.V1PodDict`

```python
from kubernetes.client.api import core_v1_api

from kubernetes_typed.client import V1PodDict

api_instance = core_v1_api.CoreV1Api()

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

api_instance.create_namespaced_pod(body=pod_manifest, namespace='default')
```

### Limitations

* Kubernetes client api functions are currently not covered by stubs, so you might get `Call to untyped function` errors. Check [mypy config doc](https://mypy.readthedocs.io/en/stable/config_file.html) on how to disable separate warnings.

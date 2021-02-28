<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>

# kubernetes-typed

[![Build status](https://github.com/gordonbondon/kubernetes-typed/workflows/Test/badge.svg?branch=master&event=push)](https://github.com/gordonbondon/kubernetes-typed/actions?query=workflow%3ATest+branch%3Amaster)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

mypy plugin to dynamically define types for Kubernetes objects.

## Features

* Type checking for [Custom Resources](#Custom-Resource-Definitions)
* Type checking for [kubernetes-client](#Kubernetes-Python-Client-types)

## Installation

Install with `pip` from source:
```shell
pip install https://github.com/gordonbondon/kubernetes-typed/archive/master.zip#egg=kubernetes-typed
```

## Custom Resource Definitions

Add type checks for [Custom Resource Definition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) spec given its definition in `yaml` file .

1. Configure `mypy` to use `crd_typed` plugin:
```ini
[mypy]

plugins = crd_typed.plugin
```

2. Import `CustomResource`

```
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

To enable full type checking for classes use provided `kubernetes_typed` plugin. Configure `mypy` to use it and it will automatically type check classes from `kubernetes.client`:

```ini
[mypy]

plugins = kubernetes_typed.plugin
```

# kubernetes-typed

mypy plugin to dynamically define types for Kubernetes objects.

# Custom Resource Definitions

Configure `mypy`:
```ini
[mypy]

plugins = crd_typed.plugin
```

Get `TypeDict` definition for custom resource body:

```python
from crd_type import CustomResource

resource: CustomResource["relative/path/to/crd.yaml"]
```

Get definition only for resource `spec`:

```python
from crd_type import CustomResource

resource: CustomResource["relative/path/to/crd.yaml", "spec"]
```

Get definition for nested spec item, if that item is type `object` or `array`:

```python
from crd_type import CustomResource

resource: CustomResource["relative/path/to/crd.yaml", "spec", "some_property"]
```

Get definition for array item, if that is array of objects, via `items` key:

```python
from crd_type import CustomResource

resource: CustomResource["relative/path/to/crd.yaml", "spec", "some_array_of_objects", "items"]
```

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

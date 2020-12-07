# Design notes

## CRD Types

Infer types from CRD [`spec.versions.0.schema.openAPIV3Schema`](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-a-customresourcedefinition) linked via `get_class_decorator_hook()`

## Kubernetes Types

Use `get_type_analyze_hook()` to provide class data for https://github.com/kubernetes-client/python core models using
their `openapi_types` attribute

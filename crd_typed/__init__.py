"""crd_typed provides mypy plugin and default class for Kubernetes CRD yaml files."""
from typing import Any, Dict


class CustomResource(Dict[Any, Any]):
    """Placeholder for Custom Resource body TypedDict."""

    def __class_getitem__(cls: Any, class_item: Any) -> Any:
        """Get actual type of a class."""
        return dict

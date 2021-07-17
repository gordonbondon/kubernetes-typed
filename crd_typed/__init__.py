from typing import Any, Dict


class CustomResource(Dict[Any, Any]):
    """Placeholder for Custom Resource body TypedDict."""

    def __class_getitem__(cls: Any, item: Any) -> Any:
        return dict

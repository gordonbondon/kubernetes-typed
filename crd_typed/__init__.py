from typing import Any, Callable, Dict, List

__all__ = ["CustomResource", "CustomResourceDict"]

_U = TypeVar("_U")


class CustomResource(Dict[Any, Any]):
    """Placeholder for Custom Resource body TypedDict."""

    def __class_getitem__(cls: Any, item: Any) -> Any:
        return dict


def CustomResourceDict(
    name: str, definition_path: str, property_path: List[str], group: str, version: str, kind: str
) -> Callable[[_U], _U]:
    """
    CustomResourceDict creates TypedDict type representing Custom Resource

    For example:
    from crd_typed import CustomResourceDict

    MyResource = CustomResourceDict(
        "MyResource"
        definition_path = "/path/to/crd.yaml",
        property_path = ["spec", "some_property"]
        group = "myapi.io",
        version = "v1",
        kind = "MyResource"
    )
    """

    def new_type(x: _U):
        return x

    new_type.__name__ = str(name)
    new_type.__supertype__ = Dict[Any, Any]
    new_type._definition_path = definition_path  # type: ignore
    new_type._property_path = property_path  # type: ignore
    new_type._group = group  # type: ignore
    new_type._version = version  # type: ignore
    new_type._kind = kind  # type: ignore

    return new_type

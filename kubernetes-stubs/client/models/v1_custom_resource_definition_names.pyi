# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1CustomResourceDefinitionNames:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, categories: Optional[Any] = ..., kind: Optional[Any] = ..., list_kind: Optional[Any] = ..., plural: Optional[Any] = ..., short_names: Optional[Any] = ..., singular: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def categories(self): ...
    @categories.setter
    def categories(self, categories: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def list_kind(self): ...
    @list_kind.setter
    def list_kind(self, list_kind: Any) -> None: ...
    @property
    def plural(self): ...
    @plural.setter
    def plural(self, plural: Any) -> None: ...
    @property
    def short_names(self): ...
    @short_names.setter
    def short_names(self, short_names: Any) -> None: ...
    @property
    def singular(self): ...
    @singular.setter
    def singular(self, singular: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

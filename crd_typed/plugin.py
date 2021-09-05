"""plugin implements mypy plugin."""
from typing import Any, Callable, Dict, List, Optional, Tuple, cast

import yaml
from jsonschema_typed.plugin import APIv4, TypeMaker
from mypy.nodes import MypyFile
from mypy.plugin import AnalyzeTypeContext, Plugin
from mypy.types import AnyType, RawExpressionType, Type, TypeOfAny, UnboundType

CUSTOM_RESOURCE_NAME = "crd_typed.CustomResource"


class CRDPlugin(Plugin):
    """Provides support for the CRD specs as TypedDict."""

    def get_type_analyze_hook(self, fullname: str) -> Optional[Callable[[AnalyzeTypeContext], Type]]:
        """Get type analyse hook callback."""
        if fullname == CUSTOM_RESOURCE_NAME:
            return custom_resource_callback

        return None

    def get_additional_deps(self, mypy_file: MypyFile) -> List[Tuple[int, str, int]]:
        """Add ``mypy_extensions`` as a dependency."""
        return [(10, "mypy_extensions", -1)]


def custom_resource_callback(ctx: AnalyzeTypeContext) -> Type:
    """Type analyze callback."""
    if not ctx.type.args:
        return ctx.type

    definition_path, *sub_schema = list(map(resolve_arg, ctx.type.args))

    openapi_schema = load_schema(definition_path)

    if openapi_schema is None:
        ctx.api.fail(
            "CustomResourceDefinition at {0} has empty schema ".format(definition_path),
            ctx.context,
        )

        return AnyType(TypeOfAny.unannotated)

    if sub_schema:
        openapi_schema = get_sub_schema(openapi_schema, sub_schema)

    if openapi_schema is None:
        ctx.api.fail(
            "CustomResourceDefinition at {0} does not have type object subschema defined for {1}".format(
                definition_path,
                sub_schema,
            ),
            ctx.context,
        )

        return AnyType(TypeOfAny.unannotated)

    make_type = TypeMaker("", openapi_schema, api_version=APIv4)

    return make_type(ctx)


def resolve_arg(argument: Any) -> str:
    """Resolve class argument to plugin settings."""
    setting: str = ""
    if isinstance(argument, RawExpressionType):
        setting = cast(str, argument.literal_value)
    elif isinstance(argument, UnboundType):
        setting = cast(str, argument.original_str_expr)

    return setting


def load_schema(path: str) -> Optional[Dict[Any, Any]]:
    """Load Custom Resource OpenAPI schema definition from a file."""
    with open(path, "r") as stream:
        version = yaml.safe_load(stream)["spec"]["versions"][0]
        schema: Dict[Any, Any] = version["schema"]["openAPIV3Schema"]

    return schema


def get_sub_schema(schema: Dict[Any, Any], keys: List[str]) -> Optional[Dict[Any, Any]]:
    """Retrieve subschema for nested object types."""
    sub_schema = schema
    for key in keys:
        try:
            if sub_schema["type"] == "object":
                sub_schema = sub_schema["properties"][key]
            elif sub_schema["type"] == "array":
                sub_schema = sub_schema[key]
        except KeyError:
            return None

    return sub_schema


def plugin(_version: str) -> Any:
    """Get mypy CRD plugin."""
    return CRDPlugin

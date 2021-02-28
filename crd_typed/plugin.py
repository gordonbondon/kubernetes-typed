from typing import Any, Callable, List, Optional, cast

import yaml
from jsonschema_typed.plugin import APIv4, TypeMaker
from mypy.plugin import AnalyzeTypeContext, Plugin
from mypy.types import AnyType, RawExpressionType, Type, TypeOfAny, UnboundType


class CRDPlugin(Plugin):
    """Provides support for the CRD specs as TypedDict."""

    CustomResource = "crd_typed.CustomResource"

    def get_type_analyze_hook(self, fullname: str) -> Optional[Callable]:
        if fullname == self.CustomResource:
            return custom_resource_callback

        return None

    def get_additional_deps(self, file):
        """Add ``mypy_extensions`` as a dependency."""
        return [(10, "mypy_extensions", -1)]


def custom_resource_callback(ctx: AnalyzeTypeContext) -> Type:
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
            "CustomResourceDefinition at {0} does not have type object subschema "
            "defined for {1}".format(definition_path, sub_schema),
            ctx.context,
        )

        return AnyType(TypeOfAny.unannotated)

    make_type = TypeMaker("", openapi_schema, api_version=APIv4)
    _type = make_type(ctx)

    return _type


def resolve_arg(value: Any) -> str:
    var: str = ""
    if isinstance(value, RawExpressionType):
        var = cast(str, value.literal_value)
    elif isinstance(value, UnboundType):
        var = cast(str, value.original_str_expr)

    return var


def load_schema(path: str) -> Optional[dict]:
    with open(path, "r") as stream:
        schema = yaml.safe_load(stream)["spec"]["versions"][0]["schema"]["openAPIV3Schema"]

    return schema


def get_sub_schema(schema: dict, keys: List[str]) -> Optional[dict]:
    _schema = schema
    for key in keys:
        try:
            if _schema["type"] == "object":
                _schema = _schema["properties"][key]
            elif _schema["type"] == "array":
                _schema = _schema[key]
        except KeyError:
            return None

    return _schema


def plugin(_version: str):
    return CRDPlugin
